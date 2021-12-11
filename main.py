import tkinter as tk
import SlmmGui
from SlmmUtils import getSlmmConfig, getSlmmLogger

# Creates config object
config = getSlmmConfig()
# Creates logger object
logger = getSlmmLogger()

def main():

    logger.debug('Starting application')

    #Creates tkinter GUI
    root = tk.Tk()
    app = SlmmGui.SlmmGui(master=root)
    app.mainloop()

    logger.debug('Exiting application')

if __name__ == "__main__":
    main()
