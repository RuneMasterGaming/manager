import os, time, urllib.request, io, webbrowser, getpass, socket, zipfile
from binascii import hexlify, unhexlify
from sys import platform
true = 'true'
false = 'false'
triffle = socket.gethostname()
if triffle == 'getcoffeebeforestarting':
    print("Triffle if you encounter a bug please screenshot the error from the terminal and send it to me.")

def log(info):
    info = str(info)
    if os.path.isfile('./log.txt') == True:
        logdata = open("log.txt", 'a')
        logdata.write(info + "\n")
    else:
        logdata = open("log.txt", 'w+')
        logdata.write(info + "\n")
    logdata.close()

def updater():
    cversion = '0.9.476.beta'
    cversion = str(cversion).split(".")
    cmv = int(cversion[len(cversion)-4])
    csv = int(cversion[len(cversion)-3])
    chf = int(cversion[len(cversion)-2])
    cmode = str(cversion[len(cversion)-1])
    urllib.request.urlretrieve("https://raw.githubusercontent.com/RuneMasterGaming/manager/master/version.txt", "version.txt")
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

    if (cmode == 'pre') or (cmode == 'beta') or (cmode == 'dev'):
        cversion = str(str(cmode) + "-" + str(cmv) + "." + str(csv) + "." + str(chf))
    else:
        cversion = str(str(cmv) + "." + str(csv) + "." + str(chf))
    verinfo = str("Latest Version: " + str(nversion) + " Current Version: " + str(cversion))
    print(verinfo)
    log(verinfo)
    if (mv > cmv) or (sv > csv) or (hf > chf):
        print("Update Available!")
        if os.path.isfile("./changelog.txt") == True:
            os.remove("changelog.txt")
        urllib.request.urlretrieve("https://raw.githubusercontent.com/RuneMasterGaming/manager/master/changelog.txt", "changelog.txt")
        changelogd = open("changelog.txt", 'r')
        changelog = changelogd.read()
        print(changelog)
        update = input("Do you want to update? [Y]es/[N]o : ")
        if (update == 'Y') or (update == 'y') or (update == 'Yes') or (update == 'yes'):
            for filename in os.listdir("."):
                if filename.startswith("manager"):
                    os.rename(filename, "manager" + cversion + ".py")
                    print("Updating to latest version...")
                    info = "Updating to latest version..."
                    log(info)
                    time.sleep(1)
                    urllib.request.urlretrieve("https://raw.githubusercontent.com/RuneMasterGaming/manager/master/manager.py", "manager.py")
            time.sleep(1)
            if platform == 'linux':
                os.system('python3 manager.py')
                exit()
            elif platform == 'win32':
                os.system('manager.py')
                exit()
        elif (update == 'N') or (update == 'n') or (update == 'No') or (update == 'no'):
            print("Not Updating")
    elif nversion == cversion:
        info = str("Currently up to date on version " + str(cversion))
        print(info)
        log(info)
    elif mode == 'dev':
        info = str("Developer Version Detected! Not Updating!")
        print(info)
        log(info)
    else:
        info = "[Error]: Unrecognized mode"
        print(info)
        log(info)
    if os.path.isfile('./version.txt') == True:
        os.remove("version.txt")
    time.sleep(2)
    ftsetup()

def ftsetup():
    if os.path.isfile('./fts.txt') == True:
        info = "fts.txt exists"
        log(info)
    else:
        info = "fts.txt doesn't exist"
        log(info)
        urllib.request.urlretrieve("https://raw.githubusercontent.com/RuneMasterGaming/manager/master/fts.txt", "fts.txt")
    fts = open('fts.txt', 'r')
    ftscheck = str(fts.read().strip())
    if ftscheck == true:
        info = "Running First Time Setup"
        print(info)
        log(info)
        fts.close
        if platform == "linux":
            print("running on linux everything should work")
            os.system("sudo pip install simple-crypt")
        elif platform == "win32":
            print("Windows OS detected installing dependencies...")
            os.system("pip install simple-crypt")
            print("Install the right version for the current python version you have.")
            print("Current Version:")
            os.system('python --verison')
            print("Launching browser...")
            time.sleep(1)
            print("after installing press any key to continue...")
            time.sleep(2)
            webbrowser.open("https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/", new=0, autoraise=True)
            import msvcrt as m
            m.getch()
        elif platform == "darwin":
            print("[WARNING]: Unsupported Version, use at your own risk!")
        print("In order for your passwords to be stored safely please Enter a master password!")
        global mpw
        mpw = getpass.getpass("Enter Password: ")
        mpwcheck = getpass.getpass("Enter again: ")
        if mpw == mpwcheck:
            print("Passwords Match!")
        else:
            print("[Error]: passwords do not match!")
        del mpwcheck
        if os.path.isfile("./.pwlist.pw") == False:
            print("password database not detected, now creating one")
            pwdb = open(".pwlist.pw", 'w+')
        else:
            pwdb = open(".pwlist.pw", 'w')
        pwdb.write("// [Entries] \n")
        pwdb.close()
        pwdb = open(".pwlist.pw", 'r')
        pwdbread = pwdb.read()
        pwdb.close()
        pwdbread = str(pwdbread)
        ciphertext = encrypt(mpw, pwdbread.encode('utf8'))
        ciphertext = hexlify(ciphertext)
        ciphertext = str(ciphertext)
        ciphertext = ciphertext.upper()
        ciphertext = ciphertext.lstrip("B'")
        ciphertext = ciphertext.rstrip("'")
        vault = open('.pwlist.pw', 'w+')
        vault.write(ciphertext)
        vault.close()
        del pwdb, pwdbread, mpw
        fts = open('fts.txt', 'w+')
        fts.write('false')
        info = "First Time Setup is finished"
        print(info)
        log(info)


    elif ftscheck == false:
        info = "Not first time running..."
        log(info)
    else:
        info = "[Error]: FTS check didn't responde with a recognizable output"
        log(info)
        fts = open('fts.txt', 'w+')
        fts.write('false')
    fts.close

try:
    import gi
    from simplecrypt import encrypt, decrypt
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk, GObject, Gdk
    updater()

    class DialogExample(Gtk.Window):
        def __init__(self, name, user, psw):
            Gtk.Window.__init__(self, title=name)
            self.set_default_size(300, 100)

            self.timeout_id = None

            entry1 = Gtk.Entry()
            entry1.set_editable(False)
            entry1.set_text(user)

            global entry2
            entry2 = Gtk.Entry()
            entry2.set_editable(False)
            entry2.set_text(psw)
            entry2.set_visibility(False)

            visibutton = Gtk.CheckButton()
            visibutton.set_label("Show Password")
            visibutton.connect("toggled", self.toggled_visibility)
            visibutton.set_active(False)

            clipboard = Gtk.Button(label="Copy")
            clipboard.connect("clicked", self.copy_clipboard)

            grid1 = Gtk.Grid()
            grid1.set_column_spacing(5)
            grid1.set_column_homogeneous(True)
            grid1.set_row_homogeneous(True)
            grid1.attach(entry1, 0, 0, 1, 1)
            grid1.attach_next_to(entry2, entry1, Gtk.PositionType.RIGHT, 1, 1)
            grid1.attach_next_to(visibutton, entry2, Gtk.PositionType.RIGHT, 1, 1)
            grid1.attach_next_to(clipboard, visibutton, Gtk.PositionType.BOTTOM, 1, 1)

            self.add(grid1)

        def toggled_visibility(self, button):
            if button.get_active():
                entry2.set_visibility(True)
            else:
                entry2.set_visibility(False)

        def copy_clipboard(self, button):
            atom = Gdk.atom_intern('CLIPBOARD', True)
            clip = entry2.get_clipboard(atom)
            clip.set_text(entry2.get_text(), -1)

            print("Copied to Clipboard")
            kill = open(".kill.py", 'w+')
            kill.write("""import time, gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, Gdk
time.sleep(20)
entry = Gtk.Entry()
atom = Gdk.atom_intern('CLIPBOARD', True)
clip = entry.get_clipboard(atom)
clip.set_text("", -1)
""")
            kill.close
            os.system("nohup python3 .kill.py &")
            print("Clipboard will be cleared after 20 seconds")


    class EntryWindow(Gtk.Window):

        def __init__(self):
            Gtk.Window.__init__(self, title="SG Password Manager v0.9")
            self.set_size_request(400, 400)

            self.timeout_id = None

            global entry
            entry = Gtk.Entry()
            entry.set_placeholder_text("Enter Master Password")
            entry.set_visibility(False)


            button = Gtk.Button(label="Unlock")
            button.connect("clicked", self.button_clicked)

            self.statusbar = Gtk.Statusbar()
            self.context_id = self.statusbar.get_context_id("example")
            self.statusbar.push(
                self.context_id, "Waiting For Password")

            grid = Gtk.Grid()
            grid.set_column_spacing(5)
            grid.set_column_homogeneous(True)
            grid.set_row_homogeneous(True)
            grid.attach(entry, 0, 0, 2, 1)
            grid.attach(button, 0, 1, 2, 1)
            grid.attach(self.statusbar, 0, 2, 2, 1)

            self.add(grid)

        def button_clicked(self, button):
            global mpw
            mpw = entry.get_text()
            self.decrypt_vault(mpw)

        def decrypt_vault(self, mpw):
            vault = open('.pwlist.pw','r')
            vaultdata = vault.read()
            vaulthex = unhexlify(vaultdata)
            vaultdec = decrypt(mpw, vaulthex)
            vaultutf = vaultdec.decode('utf8')
            pwfile = str(vaultutf)
            pwlist = open('.tmp.tmp', 'w+')
            self.load_vault(pwfile)

        def load_vault(self, pwfile):
            account = ''
            info = "Unlocking"
            print(info)
            log(info)
            pwfile2 = str(pwfile)
            pwfile2 = pwfile.strip()
            while (account != 'quit') and (account != 'add'):
                account = input("Search For Account: ")
                if (account != 'quit') and (account != 'add'):
                    for line in pwfile2.splitlines():
                        if line.startswith('//'):
                            info = "Skipping title..."
                            log(info)
                        else:
                            info = "detected proper format"
                            log(info)
                            pw = line.split(",")
                            name = pw[len(pw)-3]
                            user = pw[len(pw)-2]
                            psw = pw[len(pw)-1]
                            if name == account:
                                self.show_account(name,user,psw)
            if account == 'quit':
                info = "locking and shutting down"
                log(info)
                self.lock_vault()
            elif account == 'add':
                pwlist = open('.tmp.tmp', 'a')
                nentry = input("Enter Website: ")
                uentry = input("Enter Username: ")
                pentry = getpass.getpass("Enter Password: ")
                pentrycheck = getpass.getpass("Enter Password Again: ")
                while pentry != pentrycheck:
                    print("Passwords don't match! Try again")
                    pentry = getpass.getpass("Enter Password: ")
                    pentrycheck = getpass.getpass("Enter Password Again: ")
                entry = str(nentry + "," + uentry + "," + pentry)
                pwlist.write(pwfile)
                pwlist.write(entry + '\n')
                pwlist.close
                pwlist = open('.tmp.tmp', 'r')
                pwlistdata = pwlist.read()
                pwliststr = str(pwlistdata)
                pwlist.close
                if os.path.isfile("./.tmp.tmp") == True:
                    os.remove(".tmp.tmp")
                ciphertext = encrypt(mpw, pwliststr.encode('utf8'))
                ciphertext = hexlify(ciphertext)
                ciphertext = str(ciphertext)
                ciphertext = ciphertext.upper()
                ciphertext = ciphertext.lstrip("B'")
                ciphertext = ciphertext.rstrip("'")
                vault = open('.pwlist.pw', 'w+')
                vault.write(ciphertext)
                pwfile = pwliststr
                self.load_vault(pwfile)


        def lock_vault(self):
            print("Locking")
            if os.path.isfile("./.tmp.tmp") == True:
                os.remove('.tmp.tmp')
            exit()

        def show_account(self, name, user, psw):
            dialog = DialogExample(name, user, psw)
            dialog.connect("delete-event", Gtk.main_quit)
            dialog.show_all()
            Gtk.main()


    win = EntryWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
except ImportError:
    if os.path.isfile("./fts.txt") == True:
        os.remove('fts.txt')
    os.system("python3 run.py")
except  KeyboardInterrupt:
    info = "Shutting Down..."
    print(info)
    log(info)
    exit()