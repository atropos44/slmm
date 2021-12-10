import tkinter as tk
from tkinter import scrolledtext
import logging, logging.config, configparser
from SlmmDatabase import SlmmDatabase

# Creates config object
config = configparser.ConfigParser()
config.read('config.ini')

# Creates logger object
logging.config.fileConfig('logger.ini')
logger = logging.getLogger('SlmmLogger')

class SlmmGui(tk.Frame):
    '''
    Main class for GUI components
    '''

    def __init__(self, master=None):
        super().__init__(master)
        
        self.log_message = tk.StringVar()

        # Root window
        self.master = master
        self.master.title("Skyrim Linux Mod Manager")
        self.master.minsize(640, 480)
        self.master.option_add('*tearOff', tk.FALSE)

        # Main Frame grid 2x1
        self.mainframe = tk.Frame(self.master)
        self.mainframe.grid(column=0, row=0, sticky=(tk.NS, tk.EW))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.rowconfigure(1, weight=1)

        # Populate GUI elements
        self.create_widgets()

        logger.debug('Application GUI created')
        self.log_message.set('Ready.')

    def create_widgets(self):
        '''
        Create GUI components inside the main window
        '''

        # Menu bar
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)
        menu_bar.add_command(label="Settings", command=self.openSettings)
        menu_bar.add_command(label="Add Mod", command=self.addMod)
        menu_bar.add_command(label="Refresh", command=self.refreshGui)
        menu_bar.add_command(label="Save load order", command=self.saveLoadOrder)

        # Mods list
        mods_frame = tk.Frame(self.mainframe, bg='white')
        mods_frame.grid(column=0, row=0, sticky=(tk.N, tk.EW))
        mods_frame.columnconfigure(0, weight=1)
        mods_frame.columnconfigure(1, weight=1)
        mods_frame.columnconfigure(2, weight=1)
        mods_frame.columnconfigure(3, weight=1)
        mods_frame.rowconfigure(0, weight=1)
        # Add existing mods to the GUI list
        self.populateModsList(mods_frame)

        # Log label
        log_label = tk.Label(self.mainframe, textvariable=self.log_message, fg='grey')
        log_label.grid(column=0, row=1, sticky=(tk.W, tk.S))

    def populateModsList(self, mods_frame):
        '''
        Populate GUI mod list from elements in the DB
        '''

        tk.Label(mods_frame, text="Order", bg='dark grey').grid(column=0, row=0, sticky=tk.EW)
        tk.Label(mods_frame, text="Name", bg='dark grey').grid(column=1, row=0, sticky=tk.EW)
        tk.Label(mods_frame, text="Status", bg='dark grey').grid(column=2, row=0, sticky=tk.EW)
        tk.Label(mods_frame, text="Actions", bg='dark grey').grid(column=3, row=0, sticky=tk.EW)

        database = SlmmDatabase()
        mods_list = database.getMods()

        for idx, mod in enumerate(mods_list):
            tk.Label(mods_frame, text=str(mod.order), bg='white').grid(column=0, row=idx+1, sticky=tk.W)
            tk.Label(mods_frame, text=mod.name, bg='white').grid(column=1, row=idx+1, sticky=tk.W)
            tk.Label(mods_frame, text=mod.status, bg='white').grid(column=2, row=idx+1, sticky=tk.W)
                    
            logger.debug('Adding mod: %s' %(mod))

    def openSettings(self):
        '''
        Open Settings panel
        '''

        pass

    def addMod(self):
        '''
        Trigger actions to add a mod to the list
        '''

        pass

    def refreshGui(self):
        '''
        Refresh the main window
        '''

        pass

    def saveLoadOrder(self):
        '''
        Save changes made to the mods load order
        '''

        pass
