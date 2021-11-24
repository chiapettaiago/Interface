from tkinter import *
import webbrowser

win = Tk()
win.title("Barrra de Pesquisa")
win.geometry("300x300")


def search():
  url = entry.get()
  webbrowser.open(url)

label1 = Label(win, text="Insira o endereço do site ", font=("arial", 10, "bold"))

label1.grid(row=0, column=0)

entry = Entry(win, width=30)
entry.grid(row=0, column=1)

button = Button(win, text="Pesquisar", command=search)
button.grid(row=1, column=0, columnspan=2, pady=10)

win.mainloop()