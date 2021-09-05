from tkinter import *

root = Tk()
root.title("Intento de Calculadora")
root.geometry("328x158")
root.configure(background="#252525")

ecuacion = StringVar()

def press(num):
    ecuacion.set(ecuacion.get() + str(num))
    print(ecuacion.get())
   
def resolver():
    try:
        total = str(eval(ecuacion.get()))
        ecuacion.set(total)
    except:
        ecuacion.set("ERROR")

def cl():
    ecuacion.set("")

def set_interface():
    entrada_exp = Entry(root, textvariable=ecuacion, bg="black", fg="white").grid(row=0, columnspan=4, sticky="nswe")

    

    def numeros():
        btn9 = Button(root, text=9, width=10, padx=2, 
        pady=2, background="#262626", fg="white", command= lambda: press(9)).grid(column=2, row=1, sticky="nswe")
        btn8 = Button(root, text=8, width=10, padx=2, 
        pady=2, background="#262626", fg="white", command= lambda: press(8)).grid(column=1, row=1, sticky="nswe")
        btn7 = Button(root, text=7, width=10, padx=2, 
        pady=2, background="#262626", fg="white", command= lambda: press(7)).grid(column=0, row=1, sticky="nswe")
        btn6 = Button(root, text=6, width=10, padx=2, 
        pady=2, background="#262626", fg="white", command= lambda: press(6)).grid(column=2, row=2, sticky="nswe")
        btn5 = Button(root, text=5, width=10, padx=2, 
        pady=2, background="#262626", fg="white", command= lambda: press(5)).grid(column=1, row=2, sticky="nswe")
        btn4 = Button(root, text=4, width=10, padx=2, 
        pady=2, background="#262626", fg="white", command= lambda: press(4)).grid(column=0, row=2, sticky="nswe")
        btn3 = Button(root, text=3, width=10, padx=2, 
        pady=2, background="#262626", fg="white", command= lambda: press(3)).grid(column=2, row=3, sticky="nswe")
        btn2 = Button(root, text=2, width=10, padx=2, 
        pady=2, background="#262626", fg="white", command= lambda: press(2)).grid(column=1, row=3, sticky="nswe")
        btn1 = Button(root, text=1, width=10, padx=2, 
        pady=2, background="#262626", fg="white", command= lambda: press(1)).grid(column=0, row=3, sticky="nswe")
        btn0 = Button(root, text=0, width=10, padx=2, 
        pady=2, background="#262626", fg="white", command= lambda: press(0)).grid(column=0, row=4, sticky="nswe", columnspan=2)  
    def operaciones():
        btnDecimal = Button(root, text=".", width=10, padx=2,  command= lambda: press("."),
        pady=2, background="#536082", fg="white").grid(column=2, row=4, sticky="nswe")
        btnSuma = Button(root, text="+", width=10, padx=2, command= lambda: press("+"),
        pady=2, background="#536082", fg="white").grid(column=3, row=1, sticky="nswe")
        btnResta = Button(root, text="-", width=10, padx=2,  command= lambda: press("-"),
        pady=2, background="#536082", fg="white").grid(column=3, row=2, sticky="nswe")
        btnDivision = Button(root, text="/", width=10, padx=2,  command= lambda: press("/"),
        pady=2, background="#536082", fg="white").grid(column=3, row=4, sticky="nswe")
        btnMultiplicacion = Button(root, text="*", width=10, padx=2,  command= lambda: press("*"),
        pady=2, background="#536082", fg="white").grid(column=3, row=3, sticky="nswe")
        btnIgual = Button(root, text="=", width=10, padx=2, command= resolver,
        pady=2, background="#6C7CA8", fg="white").grid(column=3, row=5, sticky="nswe")
        btnClear = Button(root, text="Clear", width=10,  command= cl,
        padx=2, pady=2, background="#6C7CA8", fg="white").grid(column=2, row=5, sticky="nswe")
    
    btnExit = Button(root, text="Salir", background="black", fg="white", command=root.quit).grid(column=0, row=5, sticky="nswe", columnspan=2)
    numeros()
    operaciones()
    
set_interface()
#root.bind("<Return>", Calcular)
root.mainloop()