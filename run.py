import os, time, urllib.request, io
true = 'true'
false = 'false'
def updater():
    cversion = 0.4
    urllib.request.urlretrieve("https://raw.githubusercontent.com/RuneMasterGaming/manager/master/version.txt", "version.txt")
    nversion = open('version.txt', 'r')
    nversion = float(nversion.read())
    if nversion > cversion:
        os.remove("old_run.py")
        for filename in os.listdir("."):
            if filename.startswith("run"):
                os.rename(filename, "old_run.py")
                print("renamed old manager")
                time.sleep(1)
                urllib.request.urlretrieve("https://raw.githubusercontent.com/RuneMasterGaming/manager/master/run.py", "run.py")
        time.sleep(1)
        os.system("python run.py")
    elif nversion == cversion:
        print("Currently up to date on version" + str(cversion))
    else:
        print("Are you some sort of time traveler?")
    os.remove("version.txt")
    time.sleep(2)
    ftsetup()

def ftsetup():
    if os.path.isfile('./fts.txt') == True:
        print("fts.txt exists")
    else:
        print("fts.txt doesn't exist")
        urllib.request.urlretrieve("https://raw.githubusercontent.com/RuneMasterGaming/manager/master/fts.txt", "fts.txt")
    fts = open('fts.txt', 'r')
    ftscheck = str(fts.read().strip())
    if ftscheck == true:
        print("is true")
        fts.close
        config = open('config.glade', 'w+')
        fts = open('fts.txt', 'w+')
        fts.write('false')
        print("changing to false")
        print("running first time setup")
        config.write("""<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.20.0 -->
<interface>
  <requires lib="gtk+" version="3.20"/>
</interface>""")

    elif ftscheck == false:
        config = open('config.glade', 'a')
        print("is false")
    else:
        print("wtf?")
    fts.close
updater()
