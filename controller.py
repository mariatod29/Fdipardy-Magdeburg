import tkinter as tk
from view import View


class Controller(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.withdraw()
        self.view = View()

if __name__ == '__main__':
    root = tk.Tk()
    app = Controller(master=root)
    root.mainloop()
