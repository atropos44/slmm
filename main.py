import tkinter as tk
import SlmmGui
import logging, logging.config, configparser

# Creates config object
config = configparser.ConfigParser()
config.read('config.ini')

# Creates logger object
logging.config.fileConfig('logger.ini')
logger = logging.getLogger('SlmmLogger')

def main():

    logger.debug('Starting application')

    #Creates tkinter GUI
    root = tk.Tk()
    app = SlmmGui.SlmmGui(master=root)
    app.mainloop()

    logger.debug('Exiting application')

if __name__ == "__main__":
    main()
