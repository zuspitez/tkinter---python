# create a window with label using grid #

import tkinter

window = tkinter.Tk()
window.title("Face recognition system")
window.geometry("900x500")
window.configure(bg="yellow")

def close_window():
    window.destroy()

label_1=tkinter.Label(window,text="Hello world",bg="yellow",fg="red",font=('times',40,'bold'))
label_1.grid(column=0,row=0)

label_2=tkinter.Label(window,text="Hello world",bg="yellow",fg="red",font=('times',40,'bold'))
label_2.grid(column=1,row=2)

label_3=tkinter.Label(window,text="Hello world",bg="yellow",fg="red",font=('times',40,'bold'))
label_3.grid(column=2,row=4)

button1=tkinter.Button(window,text="Quit",bg="blue",fg="yellow",width=15,heigh=3,font=('times',20),command=close_window)
button1.place(x=100,y=200)


window.mainloop()