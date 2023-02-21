from tkinter import Tk, Button, Label, Entry, TOP, LEFT, BOTTOM
from Planilha import *

def remov():
    planilha['Planilha1'].pop(int(IdRemove.get()))
    for i in range(len(planilha['Planilha1'])):
        planilha['Planilha1'][i][0] = i
    salva(planilha)
    janelaRemover.destroy()

def remover():
    global janelaRemover
    janelaRemover = Tk()
    janelaRemover.title("BioDados")

    IdLabel = Label(janelaRemover,text="Digite o Id:", font=("Courier", 16, "italic"))
    IdLabel.pack(side=TOP)
    global IdRemove
    IdRemove = Entry(janelaRemover)
    IdRemove["width"] = 25
    IdRemove["font"] = ("Courier", 16, "italic")
    IdRemove.pack(side=LEFT)
    
    Remo = Button(janelaRemover, text="Remover", command=remov)
    Remo.pack(side=BOTTOM)

    janelaRemover.mainloop()
    return