import subprocess, sys, getopt, time, datetime, XenAPI

def main(argv):
    strListFile = "vmList.txt"
    strLogFile = "deploy.log"
    strWinUser = 
    strWinPassword = 
    strBinaryType = 
    strOS = "Vista_and_Above"
    strInstallMode = "Install_Only"
    installSuccessList = []
    installFailList = []
    installArgs = ""

    #usage
    def usage():
        print "Usage:"
        print
        print "install_only.py -i <vmlistfile> -o <logfile> -a <silent install arguments> -u <true | false to uninstall old agent>"
        print
        print "-h or --help"
        print
        print "-i <vmlistfile>"
        print
        print "-o <logfile>"
        print
        print "-a <silent install arguments>"
        print
        print "-u <true | false> (whether to uninstall old agent)"
        print
        print "-t <>)"
        sys.exit(2)

    #creates standardized messages for printing/logging
    def logMessage(message):
        logfileName = strLogFile
        strMessage = message
        print strMessage
        logFO = open(logfileName, "a")
        logFO.write(strMessage + "\n")
        logFO.close()
        return(0)

    #option and argument handling
    if len(sys.argv) == 1:
            print usage()
    try:
            opts, args = getopt.getopt(argv, "hi:o:m:t:s:", ["--help"])
    except getopt.GetoptError:
                usage()
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print usage()
            sys.exit()
        elif opt in ("-i"):
            strListFile = arg
        elif opt in ("-o"):
            strLogFile = arg
        elif opt in ("-m"):
            strInstallMode = arg
        elif opt in ("-t"):
            strAgentType = arg
        elif opt in ("-s"):
            strOS = arg

    logMessage("Beginning Install Script")
    print "Host list file: " + strListFile
    print "Log file: " + strLogFile
    objFile_Targets = open(strListFile)
    objFile_Log = open(strLogFile, "w+")


    #begin main body of script


    for line in objFile_Targets:
        vm = line.rstrip()
        print "Beginning installation on: " + vm

        installResultNetUse = subprocess.call(r"cmd /c net use \\" + vm + r"\c$\windows\temp /USER:" + strWinUser + " " + strWinPassword)
        installResultXCopy = subprocess.call(r"cmd /c xcopy qadeploy \\" + vm + r"\c$\windows\temp\qadeploy\ /Y")
        if strOS == "Vista_and_Above":

                if strAgentType == "FireEye_Agent":
                    installResultPath = subprocess.call(r"cmd /c set y=\"c:\ProgramData")
                    psexecCommand = r"psexec \\" + vm + " -u " + strWinUser + " -p " + strWinPassword + " -n 120 -s " + r"cmd /c c:\windows\temp\qadeploy\installer.msi /quiet /l*v install.log WINEVENTLOG_APP_ENABLE=1 WINEVENTLOG_SYS_ENABLE=1 WINEVENTLOG_SEC_ENABLE=1 WINEVENTLOG_SET_ENABLE=1 WINEVENTLOG_FWD_ENABLE=1 PERFMON=all SERVICESTARTTYPE=auto RECEIVING_INDEXER=portalsplunk.qanet.mandiant.com:9997 FORWARD_SERVER=portalspunk.qanet.mandiant.com:9997 LAUNCHSPLUNK=1 AGREETOLICENSE=Yes MONITOR_PATH=%y%"
                    installResultPsexec = subprocess.call(psexecCommand)
                if strAgentType == "MIR":
                    installResultPath = subprocess.call(r"cmd /c set y=\"c:\ProgramDatat")
                    psexecCommand = r"psexec \\" + vm + " -u " + strWinUser + " -p " + strWinPassword + " -n 120 -s " + r"cmd /c c:\windows\temp\qadeploy\installer.msi /quiet /l*v install.log WINEVENTLOG_APP_ENABLE=1 WINEVENTLOG_SYS_ENABLE=1 WINEVENTLOG_SEC_ENABLE=1 WINEVENTLOG_SET_ENABLE=1 WINEVENTLOG_FWD_ENABLE=1 PERFMON=all SERVICESTARTTYPE=auto RECEIVING_INDEXER=portalsplunk.qanet.mandiant.com:9997 FORWARD_SERVER=portalspunk.qanet.mandiant.com:9997 LAUNCHSPLUNK=1 AGREETOLICENSE=Yes MONITOR_PATH=%y%"
                    installResultPsexec = subprocess.call(psexecCommand)
                if strAgentType == "Mandiant_Agent":
                    installResultPath = subprocess.call(r"cmd /c set y=\"\ProgramData\")
                    psexecCommand = r"psexec \\" + vm + " -u " + strWinUser + " -p " + strWinPassword + " -n 120 -s " + r"cmd /c c:\windows\temp\qadeploy\installer.msi /quiet /l*v install.log WINEVENTLOG_APP_ENABLE=1 WINEVENTLOG_SYS_ENABLE=1 WINEVENTLOG_SEC_ENABLE=1 WINEVENTLOG_SET_ENABLE=1 WINEVENTLOG_FWD_ENABLE=1 PERFMON=all SERVICESTARTTYPE=auto RECEIVING_INDEXER=portalsplunk.qanet.mandiant.com:9997 FORWARD_SERVER=portalspunk.qanet.mandiant.com:9997 LAUNCHSPLUNK=1 AGREETOLICENSE=Yes MONITOR_PATH=%y%"
                    installResultPsexec = subprocess.call(psexecCommand)

        else:
            if strOS == "XP_and_2k":

                if strAgentType == "FireEye_Agent":
                    installResultPath = subprocess.call(r"cmd /c set y=\"c:\Documents and Settings\All Users\Application Data")
                    psexecCommand = r"psexec \\" + vm + " -u " + strWinUser + " -p " + strWinPassword + " -n 120 -s " + r"cmd /c c:\windows\temp\qadeploy\installer.msi /quiet /l*v install.log WINEVENTLOG_APP_ENABLE=1 WINEVENTLOG_SYS_ENABLE=1 WINEVENTLOG_SEC_ENABLE=1 WINEVENTLOG_SET_ENABLE=1 WINEVENTLOG_FWD_ENABLE=1 PERFMON=all SERVICESTARTTYPE=auto RECEIVING_INDEXER=portalsplunk.qanet.mandiant.com:9997 FORWARD_SERVER=portalspunk.qanet.mandiant.com:9997 LAUNCHSPLUNK=1 AGREETOLICENSE=Yes MONITOR_PATH=%y%"
                    installResultPsexec = subprocess.call(psexecCommand)
                if strAgentType == "MIR":
                    installResultPath = subprocess.call(r"cmd /c set y=\"c:\Documents and Settings\All Users\Application Data")
                    psexecCommand = r"psexec \\" + vm + " -u " + strWinUser + " -p " + strWinPassword + " -n 120 -s " + r"cmd /c c:\windows\temp\qadeploy\installer.msi /quiet /l*v install.log WINEVENTLOG_APP_ENABLE=1 WINEVENTLOG_SYS_ENABLE=1 WINEVENTLOG_SEC_ENABLE=1 WINEVENTLOG_SET_ENABLE=1 WINEVENTLOG_FWD_ENABLE=1 PERFMON=all SERVICESTARTTYPE=auto RECEIVING_INDEXER=portalsplunk.qanet.mandiant.com:9997 FORWARD_SERVER=portalspunk.qanet.mandiant.com:9997 LAUNCHSPLUNK=1 AGREETOLICENSE=Yes MONITOR_PATH=%y%"
                    installResultPsexec = subprocess.call(psexecCommand)
                if strAgentType == "Mandiant_Agent":
                    installResultPath = subprocess.call(r"cmd /c set y=\"c:\Documents and Settings\All Users\Application Data")
                    psexecCommand = r"psexec \\" + vm + " -u " + strWinUser + " -p " + strWinPassword + " -n 120 -s " + r"cmd /c c:\windows\temp\qadeploy\installer.msi /quiet /l*v install.log WINEVENTLOG_APP_ENABLE=1 WINEVENTLOG_SYS_ENABLE=1 WINEVENTLOG_SEC_ENABLE=1 WINEVENTLOG_SET_ENABLE=1 WINEVENTLOG_FWD_ENABLE=1 PERFMON=all SERVICESTARTTYPE=auto RECEIVING_INDEXER=portalsplunk.qanet.mandiant.com:9997 FORWARD_SERVER=portalspunk.qanet.mandiant.com:9997 LAUNCHSPLUNK=1 AGREETOLICENSE=Yes MONITOR_PATH=%y%"
                    installResultPsexec = subprocess.call(psexecCommand)
				
        
        psexecCommand = r"psexec \\" + vm + " -u " + strWinUser + " -p " + strWinPassword + " -n 120 -s " + r"cmd /c c:\windows\temp\qadeploy\installer.msi /l*v install.log"
        installResultPsexec = subprocess.call(psexecCommand)

        if installResultPsexec == 0:
            installSuccessList.append(vm)
            print "Install succeeded on: " + vm
        else:
            installFailList.append(vm)
            print "Install failed on: " + vm

    logMessage("Hosts with installation success:\n")
    if not installSuccessList:
        logMessage("\tNo successful installs.")
    else:
        for vm in installSuccessList:
            logMessage("\t" + vm)

    logMessage("\n")

    logMessage("Hosts with installation failures:\n")
    if not installFailList:
        logMessage("\tNo installation failures.")
    else:
        for vm in installFailList:
            logMessage("\t" + vm)

    logMessage("\n")

    print "End of Install Script."

if __name__ == "__main__":
    main(sys.argv[1:])

