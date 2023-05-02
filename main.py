import tkinter as tk
import GUI as g


class MainApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.withdraw()# hide default window
        self.gui = g.GUI()

if __name__ == '__main__':
    root = tk.Tk()
    app = MainApplication(master=root)
    root.mainloop()
