import tkinter as tk
from SlmmDatabase import SlmmDatabase
from SlmmUtils import getSlmmConfig, getSlmmLogger

# Creates config object
config = getSlmmConfig()
# Creates logger object
logger = getSlmmLogger()

class SlmmGui(tk.Frame):
    '''
    Main class for GUI components
    '''

    def __init__(self, master=None):
        super().__init__(master)
        
        self.status_message = tk.StringVar()
        self.skyrim_path = tk.StringVar(value=config['paths']['skyrim'])

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
        self.status_message.set('Ready.')

    def create_widgets(self):
        '''
        Create GUI components inside the main window
        '''

        # Menu bar
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)
        menu_bar.add_command(label="Settings", command=self.openSettings)
        menu_bar.add_command(label="Add Mod", command=self.addMod)
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

        # GUI status label
        status_label = tk.Label(self.mainframe, textvariable=self.status_message, fg='grey')
        status_label.grid(column=0, row=1, sticky=(tk.W, tk.S))

    def populateModsList(self, mods_frame):
        '''
        Populate GUI mod list from elements in the DB
        '''

        # Headers for mods list
        tk.Label(mods_frame, text="Order", bg='dark grey').grid(column=0, row=0, sticky=tk.EW)
        tk.Label(mods_frame, text="Name", bg='dark grey').grid(column=1, row=0, sticky=tk.EW)
        tk.Label(mods_frame, text="Status", bg='dark grey').grid(column=2, row=0, sticky=tk.EW)
        tk.Label(mods_frame, text="Actions", bg='dark grey').grid(column=3, row=0, columnspan=2, sticky=tk.EW)

        # Retrieve mods list from the database
        database = SlmmDatabase()
        mods_list = database.getMods()

        # Build mod items in the mods list
        for idx, mod in enumerate(mods_list):
            logger.debug('Adding %s' %(mod))

            tk.Label(mods_frame, text=str(mod.order), bg='white').grid(column=0, row=idx+1, sticky=tk.W)
            tk.Label(mods_frame, text=mod.name, bg='white').grid(column=1, row=idx+1, sticky=tk.W)
            tk.Label(mods_frame, text=mod.status, bg='white').grid(column=2, row=idx+1, sticky=tk.W)

            tk.Button(mods_frame, text='Load Order', command=self.changeLoadOrder(mod.id)).grid(column=3, row=idx+1, sticky=tk.E)
            tk.Button(mods_frame, text='Remove', command=self.removeMod(mod.id)).grid(column=4, row=idx+1, sticky=tk.E)
                    

    def openSettings(self):
        '''
        Open Settings panel
        '''

        logger.debug('Entering Settings panel')

        # Build Settings window
        settings_window = tk.Toplevel(self)
        settings_window.title('Settings')
        settings_window.columnconfigure(0, weight=1)
        settings_window.rowconfigure(0, weight=1)
        settings_frame = tk.Frame(settings_window)
        settings_frame.grid(column=0, row=0, sticky=(tk.NE, tk.EW))
        settings_frame.columnconfigure(1, weight=1)

        # Add settings entries from config.ini
        tk.Label(settings_frame, text="Skyrim path: ").grid(column=0, row=0, sticky=tk.W)
        tk.Entry(settings_frame, textvariable=self.skyrim_path).grid(column=1, row=0, sticky=tk.EW)

        # Build Save/Cancel buttons
        settings_button_frame = tk.Frame(settings_frame)
        settings_button_frame.grid(column=0, row=1, columnspan=2, sticky=(tk.S, tk.EW))
        settings_button_frame.rowconfigure(0, weight=1)
        settings_button_frame.columnconfigure(0, weight=1)
        settings_button_frame.columnconfigure(1, weight=1)
        tk.Button(settings_button_frame, text='Save', command=self.saveSettings).grid(column=0, row=0, sticky=(tk.S, tk.EW))
        tk.Button(settings_button_frame, text='Cancel', command=settings_window.destroy).grid(column=1, row=0, sticky=(tk.S, tk.EW))

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

    def removeMod(self, id):
        '''
        Removes a mod
        '''

        pass

    def changeLoadOrder(self, id):
        '''
        Changes the load order of a mod
        '''

        pass

    def saveSettings(self):
        '''
        Saves the settings in settings.ini
        '''

        pass