from tkinter import Toplevel, Button, Label, Entry
from Planilha import *

def insere():

    dado = [d0, d1.get(), d2.get(), d3.get(), d4.get(), d5.get()]
    planilha['Planilha1'] = planilha['Planilha1'] + [dado]
    salva(planilha)
    janelaIncerir.destroy()
    return

def Preenche():

    global janelaIncerir
    janelaIncerir = Toplevel()
    janelaIncerir.title("BioDados")

    global d0
    d0 = len(planilha['Planilha1'])

    dado1Label = Label(janelaIncerir,text="Digite o Dado1:", font=("Courier", 16, "italic"))
    dado1Label.grid(column=0, row=0, padx=10, pady=10)

    global d1
    d1 = Entry(janelaIncerir)
    d1["width"] = 25
    d1["font"] = ("Courier", 16, "italic")
    d1.grid(column=2, row=0, padx=10, pady=10)

    dado2Label = Label(janelaIncerir,text="Digite o Dado2:", font=("Courier", 16, "italic"))
    dado2Label.grid(column=0, row=1, padx=10, pady=10)

    global d2
    d2 = Entry(janelaIncerir)
    d2["width"] = 25
    d2["font"] =("Courier", 16, "italic")
    d2.grid(column=2, row=1, padx=10, pady=10)

    dado3Label = Label(janelaIncerir,text="Digite o Dado3:", font=("Courier", 16, "italic"))
    dado3Label.grid(column=0, row=2, padx=10, pady=10)

    global d3
    d3 = Entry(janelaIncerir)
    d3["width"] = 25
    d3["font"] =("Courier", 16, "italic")
    d3.grid(column=2, row=2, padx=10, pady=10)

    dado4Label = Label(janelaIncerir,text="Digite o Dado4:", font=("Courier", 16, "italic"))
    dado4Label.grid(column=0, row=3, padx=10, pady=10)

    global d4
    d4 = Entry(janelaIncerir)
    d4["width"] = 25
    d4["font"] =("Courier", 16, "italic")
    d4.grid(column=2, row=3, padx=10, pady=10)

    dado5Label = Label(janelaIncerir,text="Digite o Dado5:", font=("Courier", 16, "italic"))
    dado5Label.grid(column=0, row=4, padx=10, pady=10)

    global d5
    d5 = Entry(janelaIncerir)
    d5["width"] = 25
    d5["font"] = ("Courier", 16, "italic")
    d5.grid(column=2, row=4, padx=10, pady=10)

    Inc = Button(janelaIncerir, text="Incerir", command=insere)
    Inc.grid(column=1, row=5, padx=10, pady=10)

    return