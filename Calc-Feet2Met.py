from tkinter import *

root = Tk()
root.title("Hola mundo!")
#root.geometry("300x150")


f = Frame(root, padx=12, pady=3)
f.grid(column=0, row=0)

pies = StringVar()
pies_input = Entry(f, width=7, textvariable=pies)
pies_input.grid(column=1,row=0)

pies_input.focus()

metros = StringVar()
Label(f, textvariable=metros).grid(column=1, row=1)

def Calcular(*args):
    try:
        value = float(pies.get())
        m = int(0.3048 * value * 10000 +0.5)/10000
        metros.set(m)
    except ValueError:
        metros.set("ERROR")

Button(f, text="Calcular", command=Calcular).grid(column=2, row=2)

Label(f, text=pies).grid(column=0, row=1)
Label(f, text="es igual a").grid(column=0, row=1)
Label(f, text="metros").grid(column=2, row=1)


root.bind("<Return>", Calcular)
root.mainloop()