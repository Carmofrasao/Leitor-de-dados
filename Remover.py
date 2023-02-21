from tkinter import Toplevel, Button, Label, Entry, TOP, LEFT, BOTTOM
from Planilha import *

def remov():
    planilha['Planilha1'].pop(int(IdRemove.get()))
    for i in range(len(planilha['Planilha1'])):
        planilha['Planilha1'][i][0] = i
    salva(planilha)
    janelaRemover.destroy()

def remover():
    global janelaRemover
    janelaRemover = Toplevel()
    janelaRemover.title("BioDados")

    IdLabel = Label(janelaRemover,text="Digite o Id:", font=("Courier", 16, "italic"))
    IdLabel.grid(column=0, row=0, padx=10, pady=10)

    global IdRemove
    IdRemove = Entry(janelaRemover)
    IdRemove["width"] = 25
    IdRemove["font"] = ("Courier", 16, "italic")
    IdRemove.grid(column=0, row=1, padx=10, pady=10)
    
    Remo = Button(janelaRemover, text="Remover", command=remov)
    Remo.grid(column=0, row=2, padx=10, pady=10)

    return