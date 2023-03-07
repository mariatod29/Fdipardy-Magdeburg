from tkinter import *

root = Tk()
root.title("Fdipardy")
root.configure(background='white')
root.geometry("1500x750+100+0")

frame = Frame(root)
frame.grid()

class Fdipardy():

    def points(self):
        self.total = 0

# row 1-----------------------------------------------------------------------------------------------------------------------------------
btnSerien = Button(frame, text="Serien", width=20, height=3, font=('arial', 20, 'bold'), bd=4, bg="white").grid(row=1, column=0, pady=25)
btnNobelpreis = Button(frame, text="Nobelpreis", width=20, height=3, font=('arial', 20, 'bold'), bd=4, bg="white").grid(row=1, column=1, pady=1)
btnNahrung = Button(frame, text="Nahrung", width=20, height=3, font=('arial', 20, 'bold'), bd=4, bg="white").grid(row=1, column=2, pady=1)
btnSchah = Button(frame, text="Schah", width=20, height=3, font=('arial', 20, 'bold'), bd=4, bg="white").grid(row=1, column=3, pady=1)

# row 2-----------------------------------------------------------------------------------------------------------------------------------
btn2_1 = Button(frame, text="20$", width=20, height=2, font=('arial', 20, 'bold'), bd=4, bg="blue").grid(row=2, column=0, pady=1)
btn2_2 = Button(frame, text="20$", width=20, height=2, font=('arial', 20, 'bold'), bd=4, bg="blue").grid(row=2, column=1, pady=1)
btn2_3 = Button(frame, text="20$", width=20, height=2, font=('arial', 20, 'bold'), bd=4, bg="blue").grid(row=2, column=2, pady=1)
btn2_4 = Button(frame, text="20$", width=20, height=2, font=('arial', 20, 'bold'), bd=4, bg="blue").grid(row=2, column=3, pady=1)

# row 3-----------------------------------------------------------------------------------------------------------------------------------
btn3_1 = Button(frame, text="40$", width=20, height=2, font=('arial', 20, 'bold'), bd=4, bg="blue").grid(row=3, column=0, pady=1)
btn3_2 = Button(frame, text="40$", width=20, height=2, font=('arial', 20, 'bold'), bd=4, bg="blue").grid(row=3, column=1, pady=1)
btn3_3 = Button(frame, text="40$", width=20, height=2, font=('arial', 20, 'bold'), bd=4, bg="blue").grid(row=3, column=2, pady=1)
btn3_4 = Button(frame, text="40$", width=20, height=2, font=('arial', 20, 'bold'), bd=4, bg="blue").grid(row=3, column=3, pady=1)

# row 4-----------------------------------------------------------------------------------------------------------------------------------
btn4_1 = Button(frame, text="80$", width=20, height=2, font=('arial', 20, 'bold'), bd=4, bg="blue").grid(row=4, column=0, pady=1)
btn4_2 = Button(frame, text="80$", width=20, height=2, font=('arial', 20, 'bold'), bd=4, bg="blue").grid(row=4, column=1, pady=1)
btn4_3 = Button(frame, text="80$", width=20, height=2, font=('arial', 20, 'bold'), bd=4, bg="blue").grid(row=4, column=2, pady=1)
btn4_4 = Button(frame, text="80$", width=20, height=2, font=('arial', 20, 'bold'), bd=4, bg="blue").grid(row=4, column=3, pady=1)

# row 5-----------------------------------------------------------------------------------------------------------------------------------
btn5_1 = Button(frame, text="100$", width=20, height=2, font=('arial', 20, 'bold'), bd=4, bg="blue").grid(row=5, column=0, pady=1)
btn5_2 = Button(frame, text="100$", width=20, height=2, font=('arial', 20, 'bold'), bd=4, bg="blue").grid(row=5, column=1, pady=1)
btn5_3 = Button(frame, text="100$", width=20, height=2, font=('arial', 20, 'bold'), bd=4, bg="blue").grid(row=5, column=2, pady=1)
btn5_4 = Button(frame, text="100$", width=20, height=2, font=('arial', 20, 'bold'), bd=4, bg="blue").grid(row=5, column=3, pady=1)

root.mainloop()