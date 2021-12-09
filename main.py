import tkinter as tk
import SlmmGui

def main():
    root = tk.Tk()
    app = SlmmGui.SlmmGui(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
