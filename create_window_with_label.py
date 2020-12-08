# create a window with a label #

import tkinter as tk

window = tk.Tk()
window.title("Face recognition system")
window.geometry("900x500")

label_1=tk.Label(window,text="Hello world",font=('times',40,'bold'))
label_1.pack()

window.mainloop()