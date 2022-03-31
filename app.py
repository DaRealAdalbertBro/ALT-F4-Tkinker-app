from tkinter import *
import os
import platform

class app:
    def __init__(self, master):
        self.master = master
        master.title("Shut Down " + platform.system())
        master.geometry("412x172")
        Label(master, textvariable="What do you want the computer to do?")

        self.OPTIONS = ["Sign out", "Sleep", "Shutdown", "Restart"]
        self.defaultOption = StringVar(master)
        self.defaultOption.set(self.OPTIONS[2])

        self.menu = OptionMenu(master, self.defaultOption, *self.OPTIONS).pack(pady=5, padx=20, fill=X)
        Button(master, text="OK", command = self.OSrunCommand,
           padx=30, bg='#d6d6d6', fg='black',
           highlightcolor="#2753b8",
           highlightbackground="#2753b8",
           highlightthickness=1,
           activebackground="#dbe1ff",
           relief=FLAT, default=ACTIVE).pack(pady=10, side="top")

        Button(master, text="Cancel", command = master.destroy,
           padx=30, bg='#d6d6d6', fg='black',
           highlightcolor="#2753b8",
           highlightbackground="#2753b8",
           highlightthickness=1,
           activebackground="#dbe1ff",
           relief=FLAT, default=NORMAL).pack(side="top")
    
    def OSrunCommand(self):
        choice = self.defaultOption.get()
        if(platform.system() == "Windows"):
            if(choice == "Sign out"): os.system("shutdown /l")
            elif(choice == "Sleep"): os.system("rundll32.exe powrprof.dll, SetSuspendState Sleep")
            elif(choice == "Shut Down"): os.system("shutdown /s /t 1")
            elif(choice == "Restart"): os.system("shutdown /r /t 1")
        else:
            if(choice == "Sign out"): os.system("gnome-session-quit")
            elif(choice == "Sleep"): os.system("shutdown -H now")
            elif(choice == "Shut Down"): os.system("shutdown")
            elif(choice == "Restart"): os.system("shutdown -r")


root = Tk()
gui = app(root)
root.mainloop()