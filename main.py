# from tkinter import *
import  GUI as g
import buzzer as b
import multiprocessing as mp
# nahrung_ref = db.collection(u'nahrung')
# docs = nahrung_ref.stream()
#
# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')


# gui = g.start_gui()


#
# class MyGUI:
#     def __init__(self, master):
#         self.master = master
#         self.frame = Frame(self.master)
#         self.frame.pack()
#         self.label = Label(self.frame, text="Hello, World!")
#         self.label.pack()
#         self.button = Button(self.frame, text="Click me!", command=self.do_something)
#         self.button.pack()
#
#     def do_something(self):
#         # do something when the button is clicked
#         pass
#
#
# def main():
#     root = Tk()
#     app = MyGUI(root)
#     root.mainloop()
#
#
if __name__ == '__main__':
    p2 = mp.Process(target=b.start_buzzer, args=())
    p1 = mp.Process(target=g.start_gui, args=())
    p2.start()
    p1.start()
