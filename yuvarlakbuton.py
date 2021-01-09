from tkinter import *

pencere = Tk()
pencere.title("Yuvarlak Buton")
pencere.iconbitmap("bir.ico")
pencere.geometry("400x400")
pencere.tk_setPalette("white")

def bir():
    etiket.config(text = "1'e tıkladın.")

bir_buton = PhotoImage(file = "bir.png")

buton = Button(pencere, image=bir_buton, command=bir, borderwidth=0)
buton.pack(pady=20)

etiket = Label(pencere, text= "")
etiket.pack(pady=20)

pencere.mainloop()

