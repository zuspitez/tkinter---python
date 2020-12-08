# create a window with a quit button and the window will close when user click the quit button #

import tkinter

window = tkinter.Tk()
window.title("Face recognition system")
window.geometry("900x500")
window.configure(bg="yellow")

def close_window():
    window.destroy()

label_1=tkinter.Label(window,text="Hello world",bg="yellow",fg="red",font=('times',40,'bold'))
label_1.pack()

button1=tkinter.Button(window,text="Quit",bg="blue",fg="yellow",width=15,heigh=3,font=('times',20),command=close_window)
button1.place(x=100,y=200)


window.mainloop()