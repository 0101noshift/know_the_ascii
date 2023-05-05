from tkinter import *

window = Tk()
window.title("Averigua código ASCII")
window.geometry("330x250")
window.configure(bg="#384860")

def averiguar_ascii():
    global str_label_rta
    a = str(str_input.get())
    b = ord(a)
    str_label_rta.config(text=b)

str_label = Label(window, bg="#384860", fg="#062513", font=("Courier", 18, "bold"), text="ESCRIBA UNA LETRA,\nSÍMBOLO O UN NÚMERO\nDE UN SOLO DÍGITO:", width=20)
str_label.pack(anchor="center", pady=5, expand=1)

str_input = Entry(window, bg="light blue", fg="#062513", font=("Helvetica", 16, "bold"), width=10)
str_input.focus()
str_input.pack(anchor="center", pady=3, expand=1)

str_label_rta = Label(window, bg="#CCCCCC", fg="red", font=("Courier", 16, "bold"), text="", width=7)
str_label_rta.pack(anchor="center", pady=3, expand=1)

boton_aa = Button(window, text="AVERIGUAR", command=averiguar_ascii, width=11, height=1, bg="yellow", pady=3,font=("Courier", 12, "bold"))
boton_aa.pack()


window.mainloop()