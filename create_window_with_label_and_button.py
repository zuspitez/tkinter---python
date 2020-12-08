# create a window with a label and button #

import tkinter

window = tkinter.Tk()
window.title("Face recognition system")
window.geometry("900x500")

label_1=tkinter.Label(window,text="Hello world",font=('times',40,'bold'))
label_1.pack()

button1 = tkinter.Button(window, text="click here",width=15,heigh=3,font= ('times',20))
button1.place(x = 100, y = 200)


window.mainloop()
