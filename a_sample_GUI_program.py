# a sample GUI program #

import tkinter

window = tkinter.Tk()
window.title("Face recognition system")
window.geometry("900x500")
window.configure(bg="gold")

def close_window():
    window.destroy()

label_1=tkinter.Label(window,text="Notice: This System is for Authorized Personnel Only",bg="gold",fg="blue",font=('Helvetica',20,'bold'))
label_1.pack(anchor = "center")

button1=tkinter.Button(window,text="Face detection",bg="green",fg="yellow",width=18,height=3,font=('Helvetica',12, 'bold'),command=close_window)
button1.place(x=50,y=100)

button2=tkinter.Button(window,text="Data Collection",bg="green",fg="yellow",width=18,height=3,font=('Helvetica',12, 'bold'),command=close_window)
button2.place(x=250,y=100)

button3=tkinter.Button(window,text="Training",bg="green",fg="yellow",width=18,height=3,font=('Helvetica',12, 'bold'),command=close_window)
button3.place(x=450,y=100)

button4=tkinter.Button(window,text="Face Recognizer",bg="green",fg="yellow",width=18,height=3,font=('Helvetica',12, 'bold'),command=close_window)
button4.place(x=650,y=100)

window.mainloop()