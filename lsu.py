#!/usr/bin/python3
# Developer/Author: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# Website: https://richardneuvald.tk
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package Updater
# Version: Alpha 0.5

# Import modules
import os
import sys
import socket
import re
import uuid
import json
import logging
import stat
import subprocess
import webbrowser
import time
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import platform

# You won't get error message if you are on windows
if (platform.system() != "Windows"):
    import cpuinfo
    import psutil

# Set the file(s) rights
directory = "bash"
for file in os.listdir(directory):
    files = os.path.join(directory, file)
    os.chmod(files, stat.S_IRWXU)

# Terminal
# os.system("gnome-terminal 'bash -c \"sudo apt-get update; exec bash\"'") # It opens terminal

# LogTypes:

# () => task        @not necessary
# [] => function    @important          Do not use to gather information


def criticalLog(msg):
    logging.basicConfig(
        level=logging.CRITICAL,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/dev.log",
        filemode="a"
    )
    logging.critical(msg)


def errorLog(msg):
    logging.basicConfig(
        level=logging.ERROR,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/dev.log",
        filemode="a"
    )
    logging.error(msg)


def warningLog(msg):
    logging.basicConfig(
        level=logging.WARNING,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/dev.log",
        filemode="a"
    )
    logging.warning(msg)


def infoLog(msg):
    logging.basicConfig(
        level=logging.INFO,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/dev.log",
        filemode="a"
    )
    logging.info(msg)


def debugLog(msg):
    logging.basicConfig(
        level=logging.DEBUG,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/dev.log",
        filemode="a"
    )
    logging.debug(msg)


# LogFolder and neccesary file(s)
def createFolders():
    if (os.path.isdir("logs") != True):
        os.mkdir(os.path.join("logs"))
    if (os.path.isdir("files") != True):
        os.mkdir(os.path.join("files"))


createFolders()


def node_file():
    if (not os.path.isfile("files/node.json")):
        node = {}
        node["Node Update"] = "Disable"
        json_object = json.dumps(node, indent=3)
        with open("files/node.json", "w") as node_file:
            node_file.write(json_object)
        return json.dumps(node)


def pm2_file():
    if (not os.path.isfile("files/pm2.json")):
        pm2 = {}
        pm2["pm2 Update"] = "Disable"
        json_object = json.dumps(pm2, indent=3)
        with open("files/pm2.json", "w") as pm2_file:
            pm2_file.write(json_object)
        return json.dumps(pm2)


def forever_file():
    if (not os.path.isfile("files/forever.json")):
        forever = {}
        forever["forever Update"] = "Disable"
        json_object = json.dumps(forever, indent=3)
        with open("files/forever.json", "w") as forever_file:
            forever_file.write(json_object)
        return json.dumps(forever)


node_file()
pm2_file()
forever_file()


class Settings(tk.Toplevel):
    def __init__(self, parent):
        try:
            super().__init__(parent)

            self.geometry("300x300")
            self.title("Settings")
            self.resizable(False, False)
            self.configure(background="#383838")
            photo = PhotoImage(file="icons/setting.png")
            self.iconphoto(False, photo)

            def node_save():
                if (add_node.get() == 1):
                    try:
                        node = {}
                        node["Node Update"] = "Enable"
                        node_json_object = json.dumps(node, indent=3)
                        with open("files/node.json", "w") as f:
                            f.write(node_json_object)
                        return json.dumps(node)
                    except Exception as node_err:
                        errorLog(
                            f"Error writing node file (Enable) [node_save] - {node_err}")
                else:
                    try:
                        node = {}
                        node["Node Update"] = "Disable"
                        node_json_object = json.dumps(node, indent=3)
                        with open("files/node.json", "w") as f:
                            f.write(node_json_object)
                        return json.dumps(node)
                    except Exception as node_err:
                        errorLog(
                            "Error writing node file (Disable) [node_save] - {node_err}")

            def pm2_save():
                if (add_pm2.get() == 1):
                    try:
                        pm2 = {}
                        pm2["pm2 Update"] = "Enable"
                        pm2_json_object = json.dumps(pm2, indent=3)
                        with open("files/pm2.json", "w") as f:
                            f.write(pm2_json_object)
                        return json.dumps(pm2)
                    except Exception as pm2_err:
                        errorLog(
                            f"Error writing pm2 file (Enable) [pm2_save] - {pm2_err}")
                else:
                    try:
                        pm2 = {}
                        pm2["pm2 Update"] = "Disable"
                        pm2_json_object = json.dumps(pm2, indent=3)
                        with open("files/pm2.json", "w") as f:
                            f.write(pm2_json_object)
                        return json.dumps(pm2)
                    except Exception as pm2_err:
                        errorLog(
                            f"Error writing pm2 file (Disable) [pm2_save] - {pm2_err}")

            def forever_save():
                if (add_forever.get() == 1):
                    try:
                        forever = {}
                        forever["forever Update"] = "Enable"
                        forever_json_object = json.dumps(forever, indent=3)
                        with open("files/forever.json", "w") as f:
                            f.write(forever_json_object)
                        return json.dumps(forever)
                    except Exception as forever_err:
                        errorLog(
                            f"Error writing forever file (Enable) [forever_save] - {forever_err}")
                else:
                    try:
                        forever = {}
                        forever["forever Update"] = "Disable"
                        forever_json_object = json.dumps(forever, indent=3)
                        with open("files/forever.json", "w") as f:
                            f.write(forever_json_object)
                        return json.dumps(forever)
                    except Exception as forever_err:
                        errorLog(
                            f"Error writing forever file (Disable) [forever_save] - {forever_err}")
                    finally:
                        if (len(os.listdir("files")) != 4):
                            self.destroy()
                            messagebox.showerror(
                                "Error", "An error occurred! Please restart the application")

            # NODE
            node_strngs = open("files/node.json", "r")
            data = json.load(node_strngs)
            if (data["Node Update"] == "Enable"):
                node_opts = 1
            else:
                node_opts = 0
            node_strngs.close()

            # PM2
            pm2_strngs = open("files/pm2.json", "r")
            data = json.load(pm2_strngs)
            if (data["pm2 Update"] == "Enable"):
                pm2_opts = 1
            else:
                pm2_opts = 0
            pm2_strngs.close()

            # Forever
            forever_strngs = open("files/forever.json", "r")
            data = json.load(forever_strngs)
            if (data["forever Update"] == "Enable"):
                forever_opts = 1
            else:
                forever_opts = 0
            forever_strngs.close()

            ############################################
            # Button variables
            add_node = IntVar(value=node_opts)
            add_pm2 = IntVar(value=pm2_opts)
            add_forever = IntVar(value=forever_opts)
            ############################################

            Label(self, text="Modules", bg="#383838", fg="#FFFFFF", font=(
                'arial', 25, 'bold')).place(relx=0.5, rely=0.5, anchor=CENTER, y=-110)
            ttk.Checkbutton(self, text="Node Update", command=node_save,
                            variable=add_node, onvalue=1, offvalue=0, width=15).place(relx=0.5, rely=0.5, anchor=CENTER, y=-60)
            ttk.Checkbutton(self, text="pm2 Update", command=pm2_save,
                            variable=add_pm2, onvalue=1, offvalue=0, width=15).place(relx=0.5, rely=0.5, anchor=CENTER, y=-30)
            # ttk.Checkbutton(self, text="Forever", command=forever_save, variable=add_forever,
            #                 onvalue=1, offvalue=0, width=15).place(relx=0.5, rely=0.5, anchor=CENTER)

            def aboutSettings():
                messagebox.showinfo(
                    "How to use it?", "Please check in these modules what you want to update?")

            def aboutNode():
                webbrowser.open_new(r"https://nodejs.org/en/about/")

            def aboutPm2():
                webbrowser.open_new(r"https://pm2.keymetrics.io/")

            menu = tk.Menu(self)
            self.configure(menu=menu)
            menubar = Menu(self, background='#ffffff', foreground='black',
                           activebackground='white', activeforeground='black')

            help = Menu(menubar, tearoff=0, background='#ffffff')
            help.add_command(label="What is it?", command=aboutSettings)
            menu.add_cascade(label="Help", menu=help)

            modules = Menu(menubar, tearoff=0, background='#ffffff')
            modules.add_command(label="What is node?", command=aboutNode)
            modules.add_command(label="What is pm2?", command=aboutPm2)
            menu.add_cascade(label="Modules", menu=modules)
        except Exception as settings_err:
            criticalLog(
                f"An error occurred! The following file(s) could not be found in the settings [settings] - {settings_err}")
        finally:
            if (len(os.listdir("files")) != 4):
                self.destroy()
                self.update()
                messagebox.showerror(
                    "Error", "An error occurred! Please restart the application")


class LSU(tk.Tk):
    def __init__(self):
        super().__init__(className="Linux System Updater")

        self.title("Linux Updater")
        self.geometry("800x450+50+50")
        self.resizable(True, True)
        self.minsize(width=800, height=450)
        self.configure(background="#181d31")
        # self.iconbitmap("icons/lsu.ico")
        photo = PhotoImage(file="icons/lsu.png")
        self.iconphoto(False, photo)

        # Autolog
        # *** Data *** #
        runtime = time.strftime("%Y-%m-%d - %H:%M:%S")
        sys = platform.platform()
        py = platform.python_version()

        # Check node folder
        if (os.path.isfile("/usr/bin/node") or os.path.isfile("/usr/local/bin/node")):
            get_node_version = subprocess.check_output(['node', '-v'])
            node_version = get_node_version[:8]
        else:
            node_version = "NONE"

        def runtimeLog():
            logFile = open(f"logs/runtime.log", "a")
            logFile.write(
                f"Launched time: {runtime}\nPlatform: {sys}\nPython version: {py}\nNode version: {node_version}\n\n")
            logFile.close()
        runtimeLog()

        # About Device
        def getSystemInfo():
            try:
                info = {}
                info['Platform'] = platform.system()
                info['Platform-release'] = platform.release()
                info['Platform-version'] = platform.version()
                info['Architecture'] = platform.machine()
                info['Hostname'] = socket.gethostname()
                info['IP-address'] = socket.gethostbyname(socket.gethostname())
                info['MAC-address'] = ':'.join(re.findall('..',
                                               '%012x' % uuid.getnode()))
                # It doesn't work on windows
                if (platform.system() != "Windows"):
                    info['Processor'] = cpuinfo.get_cpu_info()['brand_raw']
                    info['RAM'] = str(
                        round(psutil.virtual_memory().total / (1024.0 ** 3)))+" GB"
                json_object = json.dumps(info, indent=3)
                with open("files/sysinfo.json", "w") as f:
                    f.write(json_object)
                return json.dumps(info)
            except Exception as sysinfo_err:
                errorLog(
                    f"An error occurred while retrieving system information [getSystemInfo] - {sysinfo_err}")
        getSystemInfo()

        def runningSystemUpdate():
            try:
                if (os.path.isfile("files/node.json")):
                    node = open('files/node.json')
                    node_data = json.load(node)
                    if (node_data["Node Update"] == "Enable"):
                        subprocess.call("bash/node_update.sh")
                    node.close()

                if (os.path.isfile("files/pm2.json")):
                    pm2 = open('files/pm2.json')
                    pm2_data = json.load(pm2)
                    if (pm2_data["pm2 Update"] == "Enable"):
                        subprocess.call("bash/pm2_update.sh")
                    pm2.close()

                subprocess.call("bash/system_update.sh")
            except Exception as upd_err:
                errorLog(
                    f"An error occurred while updating the system [runningSystemUpdate] - {upd_err}")

        def openMyWebsite():
            webbrowser.open_new(r"https://richardneuvald.tk")

        def openMyGithub():
            webbrowser.open_new(r"https://github.com/NR-SkaterBoy")

        def supportedSystem():
            messagebox.showwarning("Supported Systems",
                                   "Ubuntu, Kali Linux, Raspbian, Sparky Linux")

        def systemInfo():
            log = json.load(open("files/sysinfo.json", "r"))
            sysinfo = (f"Platform: {log['Platform']}\nPlatform-release: {log['Platform-release']}\nPlatform-version: {log['Platform-version']}\nArchitecture: {log['Architecture']}\nHostname: {log['Hostname']}\nIP-address: {log['IP-address']}\nMAC-address: {log['MAC-address']}\nProcessor: {log['Processor']}\nRAM: {log['RAM']}")
            messagebox.showinfo("System Information", sysinfo)
        # systemInfo()

        def aboutSoftware():
            messagebox.showinfo("About this project", "Most PC users stick to Windows and are not willing to change to Linux because there are fewer GUI applications and they would need to learn the basic Linux commands. Moreover, most Linux-based systems get an update every week and some people think it is a waste of time to type the update commands.\n\nThis app may come handy for both beginners and advanced users because it is able to update the system by simply clicking a button. It supports over 10 different systems and has a built-in OS recognizer.\n\nVersion: Alpha 0.5")

        def quitLSU():
            logFile = open(f"logs/runtime.log", "a")
            logFile.write(
                f"Exit time: {runtime}\n\n")
            logFile.close()
            self.protocol("WM_DELETE_WINDOW", self.quit())

        def openQuestionnaire():
            webbrowser.open_new(r"https://forms.gle/Xb5kY6cajjvRHTNB7")

        def openLastLog():
            lastLog = []
            if (not os.path.isfile("logs/runtime.log")):
                messagebox.showerror("Error", "No log file")
            else:
                with open("logs/runtime.log", encoding="utf-8") as f:
                    for line in (f.readlines()[-4:]):
                        lastLog.append(line)
                    messagebox.showinfo(
                        "Last Log", "{}{}{}{}".format(*lastLog))
        
        def openLogFile():
            try:
                os.system("gedit logs/runtime.log")
            except Exception as openLog:
                errorLog(f"Error occured while opening the file [logfile] - {openLog}")

        # Menu
        self.menubar = Menu(self, background='#ffffff', foreground='black',
                            activebackground='white', activeforeground='black')
        help = Menu(self.menubar, tearoff=0, background='#ffffff')
        help.add_command(label="Supported System", command=supportedSystem)
        help.add_command(label="About", command=aboutSoftware)
        help.add_command(label="Settings", command=self.open_settings)
        help.add_command(label="Quit", command=quitLSU)
        self.menubar.add_cascade(label="Help", menu=help)
        userHelp = Menu(self.menubar, tearoff=0, background='#ffffff')
        # Not available yet
        userHelp.add_command(label="Questionnaire", command=openQuestionnaire)
        self.menubar.add_cascade(label="News", menu=userHelp)
        info = Menu(self.menubar, tearoff=0, background='#ffffff')
        info.add_command(label="Log file", command=openLogFile)
        info.add_command(label="Last Log", command=openLastLog)
        info.add_command(label="System", command=systemInfo)
        self.menubar.add_cascade(label="Info", menu=info)
        # Title
        Label(self, text='System\nUpdater', bg="#181d31",
              fg="#ffffff", font=('arial', 40, 'bold')).place(x=60, y=25)
        # Btn of sysupdate
        Button(self, text='Update your system', bg='#F0F8FF', width=20, font=(
            'arial', 12, 'normal'), command=runningSystemUpdate).place(x=70, y=190)
        # Btn of my website
        Button(self, text='Visit my Website', bg='#F0F8FF', width=20, font=(
            'arial', 12, 'normal'), command=openMyWebsite).place(x=70, y=250)
        # Btn of my github profile
        Button(self, text='Follow me on Github', bg='#F0F8FF', width=20, font=(
            'arial', 12, 'normal'), command=openMyGithub).place(x=70, y=310)
        # Pictures
        self.lsu_pic = Canvas(self, height=470, width=449,
                              bg="#181d31", borderwidth=0, highlightthickness=0)
        self.picture_file = PhotoImage(file='pictures/lsu.png')
        self.lsu_pic.create_image(470, 0, anchor=NE, image=self.picture_file)
        self.lsu_pic.place(x=290, y=54)
        # Menu
        self.config(menu=self.menubar)

    def open_settings(self):
        settings = Settings(self)
        settings.grab_set()


if __name__ == "__main__":
    try:
        lsu = LSU()
        lsu.mainloop()
    except Exception as startup_err:
        criticalLog(
            f"An error occurred while starting the application - {startup_err}")
