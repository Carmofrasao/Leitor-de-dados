from tkinter import Tk, Button, Label, Entry
from Planilha import *

def alt():
    planilha['Planilha1'][int(IdAltera.get())] = [IdAltera.get(), d1a.get(), d2a.get(), d3a.get(), d4a.get(), d5a.get()]

    salva(planilha)
    janelaAltera.destroy()
    janelaAlterar.destroy()

def altera():
    global janelaAltera
    janelaAltera = Tk()
    janelaAltera.title("BioDados")

    dado1Label = Label(janelaAltera,text="Digite o Dado1:", font=("Courier", 16, "italic"))
    dado1Label.grid(column=0, row=0, padx=10, pady=10)

    global d1a
    d1a = Entry(janelaAltera)
    d1a.insert(0, planilha['Planilha1'][int(IdAltera.get())][1])
    d1a["width"] = 25
    d1a["font"] = ("Courier", 16, "italic")
    d1a.grid(column=2, row=0, padx=10, pady=10)

    dado2Label = Label(janelaAltera,text="Digite o Dado2:", font=("Courier", 16, "italic"))
    dado2Label.grid(column=0, row=1, padx=10, pady=10)

    global d2a
    d2a = Entry(janelaAltera)
    d2a.insert(0, planilha['Planilha1'][int(IdAltera.get())][2])
    d2a["width"] = 25
    d2a["font"] = ("Courier", 16, "italic")
    d2a.grid(column=2, row=1, padx=10, pady=10)

    dado3Label = Label(janelaAltera,text="Digite o Dado3:", font=("Courier", 16, "italic"))
    dado3Label.grid(column=0, row=2, padx=10, pady=10)

    global d3a
    d3a = Entry(janelaAltera)
    d3a.insert(0, planilha['Planilha1'][int(IdAltera.get())][3])
    d3a["width"] = 25
    d3a["font"] = ("Courier", 16, "italic")
    d3a.grid(column=2, row=2, padx=10, pady=10)

    dado4Label = Label(janelaAltera,text="Digite o Dado4:", font=("Courier", 16, "italic"))
    dado4Label.grid(column=0, row=3, padx=10, pady=10)

    global d4a
    d4a = Entry(janelaAltera)
    d4a.insert(0, planilha['Planilha1'][int(IdAltera.get())][4])
    d4a["width"] = 25
    d4a["font"] = ("Courier", 16, "italic")
    d4a.grid(column=2, row=3, padx=10, pady=10)

    dado5Label = Label(janelaAltera,text="Digite o Dado5:", font=("Courier", 16, "italic"))
    dado5Label.grid(column=0, row=4, padx=10, pady=10)

    global d5a
    d5a = Entry(janelaAltera)
    d5a.insert(0, planilha['Planilha1'][int(IdAltera.get())][5])
    d5a["width"] = 25
    d5a["font"] = ("Courier", 16, "italic")
    d5a.grid(column=2, row=4, padx=10, pady=10)

    Inc = Button(janelaAltera, text="Alterar", command=alt)
    Inc.grid(column=1, row=5, padx=10, pady=10)

    janelaAltera.mainloop()
    return

def alterar():
    global janelaAlterar
    janelaAlterar = Tk()
    janelaAlterar.title("BioDados")

    IdLabel = Label(janelaAlterar,text="Digite o Id:", font=("Courier", 16, "italic"))
    IdLabel.grid(column=0, row=0, padx=10, pady=10)
    
    global IdAltera
    IdAltera = Entry(janelaAlterar)
    IdAltera["width"] = 25
    IdAltera["font"] = ("Courier", 16, "italic")
    IdAltera.grid(column=0, row=1, padx=10, pady=10)
    
    Remo = Button(janelaAlterar, text="Alterar", command=altera)
    Remo.grid(column=0, row=2, padx=10, pady=10)

    janelaAlterar.mainloop()
    return