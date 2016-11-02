import os, time, urllib.request, io, webbrowser, getpass
from binascii import hexlify, unhexlify
from sys import platform
true = 'true'
false = 'false'
def updater():
    cversion = '0.9.462.beta'
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
    print("Latest Version: " + str(nversion) + " Current Version: " + str(cversion))
    if (mv > cmv) or (sv > csv) or (hf > chf):
        if os.path.isfile("./old_run.py") == True:
            os.remove("old_run.py")
        else:
            for filename in os.listdir("."):
                if filename.startswith("run"):
                    os.rename(filename, "old_run.py")
                    print("Updating to latest version...")
                    time.sleep(1)
                    urllib.request.urlretrieve("https://raw.githubusercontent.com/RuneMasterGaming/manager/master/run.py", "run.py")
            time.sleep(1)
            if platform == 'linux':
                os.system('python3 run.py')
            elif platform == 'win32':
                os.system('run.py')
    elif nversion == cversion:
        print("Currently up to date on version " + str(cversion))
    elif mode == 'dev':
        print("Developer Version Detected! Not Updating!")
    else:
        print("[Error]: Unrecognized mode")
    if os.path.isfile('./version.txt') == True:
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
        fts = open('fts.txt', 'w+')
        fts.write('false')
        print("changing to false")
        print("running first time setup")
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
            print("Passowrds Match!")
        else:
            print("[Error]: passwords do not match!")
        del mpwcheck
        if os.path.isfile("./.pwlist.pw") == True:
            print("password database not detected, now creating one")
            pwdb = open(".pwlist.pw", 'w+')
            pwdb.write("[Entries] \n")
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


    elif ftscheck == false:
        print("is false")
    else:
        print("wtf?")
    fts.close

if platform == 'linux':
    try:
        updater()
        import gi
        from simplecrypt import encrypt, decrypt
        gi.require_version('Gtk', '3.0')
        from gi.repository import Gtk, GObject, Gdk

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
                print("Unlocking")
                pwfile2 = str(pwfile)
                pwfile2 = pwfile.strip()
                while (account != 'quit') and (account != 'add'):
                    account = input("Search For Account: ")
                    for line in pwfile2.splitlines():
                        pw = line.split(",")
                        name = pw[len(pw)-3]
                        user = pw[len(pw)-2]
                        psw = pw[len(pw)-1]
                        if name == account:
                            self.show_account(name,user,psw)
                if account == 'quit':
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
        os.remove('fts.txt')
        os.system("python3 run.py")
    except  KeyboardInterrupt:
        print("Shutting Down")
        exit()

elif platform == 'win32':
    def windows(pwfile):
        account = ''
        print("Unlocking")
        pwfile2 = str(pwfile)
        pwfile2 = pwfile.strip()
        while (account != 'quit') and (account != 'add'):
            account = input("Search For Account: ")
            for line in pwfile2.splitlines():
                pw = line.split(",")
                name = pw[len(pw)-3]
                user = pw[len(pw)-2]
                psw = pw[len(pw)-1]
                if name == account:
                    print('Website: ' + str(name))
                    print('Username: ' + str(user))
                    print('Password: ' + str(psw))
        if account == 'quit':
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
            pwlist.write(pwfile)
            pwlist.write(entry + '\n')
            pwlist.close
            pwlist = open('.tmp.tmp', 'r')
            pwlistdata = pwlist.read()
            print(pwlistdata)
            pwliststr = str(pwlistdata)
            ciphertext = encrypt(mpw, pwliststr.encode('utf8'))
            ciphertext = hexlify(ciphertext)
            ciphertext = str(ciphertext)
            ciphertext = ciphertext.upper()
            ciphertext = ciphertext.lstrip("B'")
            ciphertext = ciphertext.rstrip("'")
            vault = open('.pwlist.pw', 'w+')
            vault.write(ciphertext)
            pwfile = pwliststr
            windows(pwfile)


    def win_decrypt():
        mpw = getpass.getpass("Please Enter Master Password")
        vault = open('.pwlist.pw','r')
        vaultdata = vault.read()
        vaulthex = unhexlify(vaultdata)
        vaultdec = decrypt(mpw, vaulthex)
        vaultutf = vaultdec.decode('utf8')
        vaultstr = str(vaultutf)
        pwlist = open('.tmp.tmp', 'w+')
        pwlist.write(vaultstr)
        pwfile = vaultstr
        windows(pwfile)

    try:
        updater()
        print("Running on Windows no gui support")
        win_decrypt()
    except KeyboardInterrupt:
        print("Closing")
