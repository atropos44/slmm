import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class SlmmGui(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Skyrim Linux Mod Manager")
        self.master.minsize(640, 480)
        self.master.option_add('*tearOff', tk.FALSE)

        # Main Frame grid 2x1
        self.mainframe = ttk.Frame(self.master, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(tk.NS, tk.EW))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=3)
        self.mainframe.rowconfigure(1, weight=1)

        self.create_widgets()

    def create_widgets(self):

        # Menu bar
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)
        menu_bar.add_command(label="Settings", command=self.openSettings)
        menu_bar.add_command(label="Add Mod", command=self.addMod)
        menu_bar.add_command(label="Refresh", command=self.refreshGui)
        menu_bar.add_command(label="Save", command=self.saveChanges)

        # Mods list
        mods_frame = ttk.Frame(self.mainframe)
        mods_frame.grid(column=0, row=0, sticky=(tk.N, tk.EW))
        mods_frame.columnconfigure(0, weight=1)
        mods_frame.rowconfigure(0, weight=1)
        
        tk.Label(mods_frame, text="Mods list").grid(column=0, row=0, sticky=tk.W)

        # Logs panel
        logs_frame = ttk.Frame(self.mainframe)
        logs_frame.grid(column=0, row=1, sticky=(tk.NS, tk.EW))
        logs_frame.columnconfigure(0, weight=1)
        logs_frame.rowconfigure(0, weight=1)
        
        tk.Label(logs_frame, text="Logs").grid(column=0, row=0, sticky=tk.W)
        logs_messages = scrolledtext.ScrolledText(logs_frame)
        logs_messages.grid(column=0, row=1, sticky=(tk.NS, tk.EW))
        logs_messages.config(bg='white', state ='disabled')

    def openSettings(self):
        pass

    def addMod(self):
        pass

    def refreshGui(self):
        pass

    def saveChanges(self):
        pass
