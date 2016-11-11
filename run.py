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
        yes = False
        while yes != True:
            if (os.path.isfile("./file.pt1")) and (os.path.isfile("./file.pt2")) and (os.path.isfile("./file.pt3")) and (os.path.isfile("./file.pt4")):
                yes = True
            else:
                urllib.request.urlretrieve("https://raw.githubusercontent.com/RuneMasterGaming/manager/master/file.pt1", "file.pt1")
                urllib.request.urlretrieve("https://raw.githubusercontent.com/RuneMasterGaming/manager/master/file.pt2", "file.pt2")
                urllib.request.urlretrieve("https://raw.githubusercontent.com/RuneMasterGaming/manager/master/file.pt3", "file.pt3")
                urllib.request.urlretrieve("https://raw.githubusercontent.com/RuneMasterGaming/manager/master/file.pt4", "file.pt4")
        if os.path.isfile("./config.txt"):
            config = open("config.txt", 'r')
            config = config.read()
            config.close()
            conf = str(config)
            for line in conf.splitlines():
                if line.startswith("[Key]"):
                    line = line.split(":")
                    keyloc = str(line[len(line)-1])
                    keyloc = keyloc.strip("'")
            if os.path.isfile(keyloc):
                keyfile = open('Decrypt.key', 'r')
                keydata = keyfile.read()
                keyfile.close()
                keystr = str(keydata)
                keylist = keystr.split(",")
                k1 = str(keylist[len(keylist)-5])
                k2 = str(keylist[len(keylist)-4])
                k3 = str(keylist[len(keylist)-3])
                k4 = str(keylist[len(keylist)-2])
                k5 = str(keylist[len(keylist)-1])
            else:
                exit()
            pt1 = open('file.pt1', 'r')
            pt1r = pt1.read()
            pt1h = unhexlify(pt1r)
            pt1d = decrypt(k1, pt1h)
            pt1u = pt1d.decode('utf8')
            pt1str = str(pt1u)

            pt2 = open('file.pt2', 'r')
            pt2r = pt2.read()
            pt2h = unhexlify(pt2r)
            pt2d = decrypt(k2, pt2h)
            pt2u = pt2d.decode('utf8')
            pt2str = str(pt2u)

            pt3 = open('file.pt3', 'r')
            pt3r = pt3.read()
            pt3h = unhexlify(pt3r)
            pt3d = decrypt(k3, pt3h)
            pt3u = pt3d.decode('utf8')
            pt3str = str(pt3u)

            pt4 = open('file.pt4', 'r')
            pt4r = pt4.read()
            pt4h = unhexlify(pt4r)
            pt4d = decrypt(k4, pt4h)
            pt4u = pt4d.decode('utf8')
            pt4str = str(pt4u)

            ourpowerscombined = str(pt1str + pt2str + pt3str + pt4str)
            OhBoy = unhexlify(ourpowerscombined)
            OHSHIT = decrypt(k5, OhBoy)
            AHHHHH = OHSHIT.decode('utf8')
            REEEEEE = str(AHHHHH)
            for filename in os.listdir("."):
                if (filename == "manager.py") and (updatedata == 0):
                    archive = str("manager-" + cversion + '.zip')
                    backup = zipfile.ZipFile(archive, 'w')
                    backup.write('manager.py')
                    backup.close()
                    if os.path.isfile("./manager.py"):
                        os.remove("manager.py")
                    time.sleep(1)
                    phewimokaynow = open('manager.py', 'w+')
                    phewimokaynow.write(REEEEEE)
                    phewimokaynow.close()
                    updatedata = 1
                time.sleep(1)
                print("Update Complete")
            if platform == 'linux':
                os.system('python3 manager.py')
                exit()
            elif platform == 'win32':
                os.system('manager.py')
                exit()

updater()
