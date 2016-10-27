import os, time, urllib.request, io, webbrowser
from sys import platform
true = 'true'
false = 'false'
def updater():
    cversion = 0.8
    urllib.request.urlretrieve("https://raw.githubusercontent.com/RuneMasterGaming/manager/master/version.txt", "version.txt")
    nversion = open('version.txt', 'r')
    nversion = float(nversion.read())
    print("Latest Version: " + str(nversion) + " Current Version: " + str(cversion))
    if nversion > cversion:
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
    else:
        print("Developer Version Detected! Not Updating!")
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
        config = open('config.glade', 'w+')
        fts = open('fts.txt', 'w+')
        fts.write('false')
        print("changing to false")
        print("running first time setup")
        os.system("sudo pip install simple-crypt")
        if platform == "linux":
            print("running on linux everything should work")
        elif platform == "win32":
            print("Windows OS detected please download this installer, scan for viruses if needed...")
            print("Launching browser...")
            time.sleep(1)
            print("after installing press any key to continue...")
            time.sleep(2)
            webbrowser.open("https://sourceforge.net/projects/pygobjectwin32/files/?source=navbar", new=0, autoraise=True)
            import msvcrt as m
            m.getch()
        elif platform == "darwin":
            print("[WARNING]: Unsupported Version, use at your own risk!")
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

try:
    updater()
    import gi
    from simplecrypt import encrypt, decrypt
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk, GObject
except ImportError:
    os.remove('fts.txt')
    if platform == 'linux':
        os.system('python3 run.py')
    elif platform == 'win32':
        os.system('run.py')

class EntryWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="SG Password Manager v0.7")
        self.set_size_request(400, 400)

        self.timeout_id = None

        global entry
        entry = Gtk.Entry()
        entry.set_placeholder_text("Enter Master Password")
        entry.set_visibility(False)


        button = Gtk.Button(label="Launch")
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
        mpw = entry.get_text()
        self.decrypt_vault(mpw)

    def decrypt_vault(self, mpw):
        print("triffle is a scrub")

win = EntryWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
