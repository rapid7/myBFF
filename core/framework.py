#! /usr/bin/python
import argparse
from fingerprint import Fingerprint
import sys
from Logger import Logger

class Framework():
    def __init__(self):
        self.config = {}
    def runner(self, argv):
        fingerprint = Fingerprint()
        fingerprint.connect(self.config)
    def parseParameters(self, argv):
        parser = argparse.ArgumentParser()
        filesgroup = parser.add_argument_group('inputs')
        filesgroup.add_argument("--host",
            dest="HOST",
            action="store",
            required=True,
            help="Host to test against")
        filesgroup.add_argument("-u",
            dest="USERNAME",
            action="store",
            help="Username")
        filesgroup.add_argument("-p",
            dest="PASSWORD",
            action="store",
            help="Password")
        filesgroup.add_argument("--domain",
            dest="domain",
            action="store",
            required=False,
            help="Domain (Used for domain logins)")
        filesgroup.add_argument("-U",
            dest="UserFile",
            action="store",
            help="File containing Usernames")
        filesgroup.add_argument("-t",
            dest="threads",
            action="store",
            help="Number of threads to use for brute forcing. (not yet implemented.)")
        filesgroup.add_argument("-o",
            dest="output",
            action="store",
            help="File to output results to.")
        filesgroup.add_argument("--vhost",
            dest="vhost",
            action="store",
            help="Virtual Directory (i.e., for rapid7.com/owa enter owa). This is used for fingerprinting purposes only.")
        args = parser.parse_args()
        self.config["USERNAME"] = args.USERNAME
        self.config["PASSWORD"] = args.PASSWORD
        self.config["HOST"] = args.HOST
        self.config["domain"] = args.domain
        self.config["UserFile"] = args.UserFile
        self.config["threads"] = args.threads
        self.config["output"] = args.output
        self.config["vhost"] = args.vhost
        if ((self.config["UserFile"] == "") and (self.config["USERNAME"] == "") and (self.config["PASSWORD"] == "")):
            print "Either -u and -p both must be set or -U must be set"
            parser.print_help()
            sys.exit(1)

    def banner(self, argv):
        print """



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
               .. """
        print " ---a Brute Force Framework by l0gan (@kirkphayes)"
    def run(self, argv):
        self.parseParameters(argv)
        if self.config["output"]:
            writer = Logger(sys.stdout, self.config["output"])
            sys.stdout = writer
        self.banner(self)
        if self.config["threads"]:
            print("This function has not been implemented yet. Threads will be set to 1...Sorry...")
        self.runner(self)
