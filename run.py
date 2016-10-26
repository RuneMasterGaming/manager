import os, time, urllib.request, signal
cversion = 0.2
urllib.request.urlretrieve("https://raw.githubusercontent.com/RuneMasterGaming/manager/master/version.txt", "version.txt")
nversion = open('version.txt', 'r')
nversion = float(nversion.read())
if nversion > cversion:
    for filename in os.listdir("."):
        if filename.startswith("run"):
            os.rename(filename, "old_run.py")
            print("renamed old manager")
            time.sleep(1)
            urllib.request.urlretrieve("https://raw.githubusercontent.com/RuneMasterGaming/manager/master/run.py", "run.py")
    os.system("nohup python run.py &")
    time.sleep(1)
    os.kill(os.getppid(), signal.SIGHUP)
elif nversion == cversion:
    print("Currently up to date!")
else:
    print("Are you some sort of time traveler?")
time.sleep(2)
