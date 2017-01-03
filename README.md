# myBFF - a Brute Force Framework
```
                         `.-:-.`           `.-::-.`
                     `:oyhhyooooo+:`    -+osooooyhhs+.
                   `/yhhs:`      `.-.`-/:.      `./syyo.
                  `shyy:            `-.            .+yyy.
    \M:         `ohyy/             `               `/yys
    :M:          .hyyy-                              .yyy.
    :M:          -hyyy/                              .hhy`
    :M:          `shyyy:                            `ohh+
    :M:           .shyyy+.                         .shh+`
    :M:            .+hhhyyo-`                    `/yho-
    :M:             `-ohhhhhy+-`               .+yy+-
    /M:              `./syhhhhs/.          -/os+-`
                         `.-+syddho-     `:+/-`
                             `.-+yddo.  `/.
                                 `-ohh- ``
                                   `-yh.
                                     .yo
                                      -s
                                      ./
                                      `
                               -.`--:--:..`         -.//:.:-////://:.`/o/ `.-/:--::///:://-.`o+-
                              .hNdNNdyhmNmds.       .sMMMmMmyhhosshdm+NMh `-dMMNNMdyhyosyhdyyMM/
                               /MMNN:  .hMMMs        oMMMMMo       `:-NM-   dMMMMN-       `:oMd`
                               .MMMN-   +MMm-        /MMMMd`         `hM`   yMMMMo          .Mh
                               `MNNM+ .:mMs+`        -NMMMd       ``  sm`   sMMMMo       .   No
                               `NMMNsymMMh--``       `yMMMd      .yo  :o    .NMMM+     `:d.  s-
                               `dMMMMMMMMNMMddho:    -NMMMy    `sNM-  .:    oMMMM:    .dNh`  :.
                               .NMMmMd++//omMMMMM-   `NMMMNo+-+hMMm         /MMMMd+/:omMMo
                               `MMNmM:     -NMMMM/   /MMMMMNdmNNMMd         yMMMMMmdmNMMM+
                               `mmNds       sMMMM.   -MMMMm.``.:sNm         sMMMMs``..:dMo
                               `hNNm:       +MMMN`   `mMMMy`     -y`        :MMMM/     `+s
                               -MNmM:       :MMMy    -NMMMh.       `        oMMMMo
                               .NmMM+       yMMd`    `hMMMm`                -NMMMs
  yms`.:+o` `-//`               hNMMs       hMN/     .mMMMd                 +MMMM+
  sMNssoNMhyyodmh``dm/   -+yh`  oNMNd      .dM:      `hMMMm`                :NMMMs
  /md`  +MMo  `:N: mN.    omo  `NMMMh    `sNms       :dMMMm                 oNMMMo
   dd   `mM.   -N+ sd     oMo   hMMMN/-/yddo/        :MMMMm.                sMMMMh
  .N+    /N:   sMs ym-``-oNMo  .mMMMNdmds.           /MMMMM+`               yMMMMm:
  /ms:  `oh:   /hh-:ydyyo/+No ::/yhoso:`             ohdhydhs/             `hddyhdyo.
                      `   :No                                `                     `
                          `mo
                          `mo
                          `mo
                 :-      `sN:
                ++      -yNo
               oy   `-+hh+.
              -mdoooo+-`
               ..`
--- A Brute Force Framework by Kirk Hayes (l0gan)
--- myBFF v1.5.1
```
myBFF is a web application brute force framework (currently)

Point the framework at a file containing usernames, a host, and give it a password. The framework will determine what type of web application is in use, then attempt to brute force accounts. After brute forcing accounts, myBFF will then do a little more, like enumerating apps available, and reading in important data. Each module is different so try them out!

## Current modules:

- HP SiteScope (will attempt to give you a Meterpreter Shell!)
- Citrix Gateway (also enumerates authorized applications)
- Juniper Portal (Will look for 2FA bypass and list what is accessible)
- MobileIron (Unknown. Have to find out what is accessible first!)
- Outlook/Office365 (will parse email, contacts, and other data from email)
- Wordpress (Will be adding "SomethingCool" soon)
- CiscoVPN (Enumerate User accounts (May not work on all configurations))
- Okta (Enumerate Applications and check if 2FA is setup for account)
- Jenkins (Will be adding "Something Cool" soon)
- SMB (Check if user is an administrator) (must use --domain with this module. for host, use smb://)
- FTP (List root dir contents)

New modules will be added.

## CONFIGURATION
myBFF requires lxml and pysmb. 

Install using 

'sudo apt-get install python-lxml'

'sudo pip install pysmb'

## USE:
https://github.com/MooseDojo/myBFF/wiki/Use
```
python myBFF.py --host https://example.com -U userfile.txt -p password123
--host - Host including protocol. Protocols currently support http, https, and smb only.
-u <username> - test single username
-U <usernameFile> - username file
-p <password> - password
-P <passwordFile> - password file
-d - dry run mode (skip somethingCool/password guessing only)
--vhost <virtualDirectory> (optional) - virtual hosting. This is for when you have a site where https://example.com goes to one page, but https://example.com/owa goes to another
-o <outputFile> - output file
--timeout <value> - timeout (Used to pause during password file attacks.)
```

## Planned Development:

See: https://github.com/MooseDojo/myBFF/wiki/Future-Plans
