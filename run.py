import os, time, urllib.request, io, webbrowser, getpass, socket, zipfile

def updater():
    print("""[New Updater]
A new version of the password manager has been made that your version cannot update to on its own.

your updater has downloaded this script which will allow it to update to the lastest version without need to manually download the new one

sit back, relax and press enter when asked.""")
    if os.path.isfile("./changlog.txt") == True:
        os.remove("changlog.txt")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/RuneMasterGaming/manager/master/changelog.txt", "changelog.txt")
    log = open("changelog.txt", 'r')
    changelog = log.read()
    log.close
    print(changelog)
    cont = input("Press enter to continue")
    if cont != 'quit':
        urllib.request.urlretrieve("https://raw.githubusercontent.com/RuneMasterGaming/manager/master/nversion.txt", "version.txt")
        nversiondata = open('version.txt', 'r')
        nversionreadun = nversiondata.read()
        nversiondata.close()
        nversionread = str(nversionreadun).strip()
        nversion = str(nversionread).split(".")
        mv = int(nversion[len(nversion)-4])
        sv = int(nversion[len(nversion)-3])
        hf = int(nversion[len(nversion)-2])
        mode = str(nversion[len(nversion)-1])
        if (mode == 'pre') or (mode == 'beta') or (mode == 'dev'):
            nversion = str(str(mode) + "-" + str(mv) + "." + str(sv) + "." + str(hf))
        else:
            nversion = str(str(mv) + "." + str(sv) + "." + str(hf))
        print("Updating you to version " + nversion + " Please wait")
        if os.path.isfile("./old_run.py") == True:
            os.remove("old_run.py")
        urllib.request.urlretrieve("https://raw.githubusercontent.com/RuneMasterGaming/manager/master/manager.py", "manager.py")
        if os.path.isfile("./manager.py"):
            print("Update complete now launching...")
            os.system("python3 manager.py")
        else:
            print("Update Failed...")

updater()
