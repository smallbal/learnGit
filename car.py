from tkinter import *


def hello():
    say_some_word()


def say_some_word():
    print('FUCK')
tk = Tk()
some_word = 'FUCK'
btn = Button(tk, text="fuck me", command=hello)
btn.pack()

tk.mainloop()
