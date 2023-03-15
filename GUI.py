from tkinter import *


def create_button(frame, text, command):
    return Button(frame, text=text, command=command, width=20, height=2, font=('Mistral 25 bold'), bd=4, fg="yellow",
                  bg="purple")


def start_gui():
    root = Tk()
    root.title("Fdipardy")
    root.configure(background='white')
    root.geometry("1435x650+100+0")

    frame = Frame(root)
    frame.grid()
    frame.pack(fill=X)

    def open_on_click():
        new = Toplevel(root)
        new.geometry("750x250")
        new.title("Question")
        Label(new, text="Question / Answer", font='Mistral 18 bold').place(x=150, y=80)

    txtDisplay = Label(frame, text="Welcome to Fdipardy", font=('Mistral 25 bold '), bg="white", bd=10, width=82,
                       justify=CENTER)
    txtDisplay.grid(row=0, column=0, columnspan=5, pady=1)

    categories = ["Serien", "Nobelpreis", "Nahrung", "Schah"]
    labels = []
    for i, category in enumerate(categories):
        label = Label(frame, text=category, width=20, height=3, font=('Mistral 25 bold'), bd=4, bg="white")
        label.grid(row=1, column=i, pady=25)
        # label.pack(fill=X)
        labels.append(label)

    btn_texts = ["20$", "20$", "20$", "20$", "40$", "40$", "40$", "40$", "80$", "80$", "80$", "80$"]
    btn_commands = [open_on_click] * len(btn_texts)

    row = 2
    col = 0
    for text, command in zip(btn_texts, btn_commands):
        button = create_button(frame, text, command)
        button.grid(row=row, column=col, pady=1)
        # button.pack
        col += 1
        if col > 3:
            col = 0
            row += 1

    root.mainloop()  # start the main event loop of the tkinter window


# start_gui()
