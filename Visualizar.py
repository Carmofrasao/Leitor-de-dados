from tkinter import Tk, Button, Label, Entry
from Planilha import *

def exvis():
    janelaVisu.destroy()

def visualizar():
    global janelaVisu
    janelaVisu = Tk()
    janelaVisu.title("BioDados")
    for i in range(len(planilha['Planilha1'][0])):
        cabecalho = Label(janelaVisu, text=planilha['Planilha1'][0][i], font=("Courier", 16, "italic"))
        cabecalho.grid(column=i, row=0, padx=10, pady=10)
        texto = Label(janelaVisu, text=planilha['Planilha1'][int(IdBusca.get())][i], font=("Courier", 16, "italic"))
        texto.grid(column=i, row=1, padx=10, pady=10)
    Visu = Button(janelaVisu, text="Ok", command=exvis)
    Visu.grid(column=int(len(planilha['Planilha1'][0])/2), row=2, padx=10, pady=10)
    janelaVisu.mainloop()
    return

def buscar():
    janelaBusca = Tk()
    janelaBusca.title("BioDados")

    IdLabel = Label(janelaBusca,text="Digite o Id:", font=("Courier", 16, "italic"))
    IdLabel.grid(column=int(len(planilha['Planilha1'][0])/2), row=0, padx=10, pady=10)
    global IdBusca
    IdBusca = Entry(janelaBusca)
    IdBusca["width"] = 25
    IdBusca["font"] = ("Courier", 16, "italic")
    IdBusca.grid(column=int(len(planilha['Planilha1'][0])/2), row=1, padx=10, pady=10)

    Visu = Button(janelaBusca, text="visualizar", command=visualizar)
    Visu.grid(column=int(len(planilha['Planilha1'][0])/2), row=2, padx=10, pady=10)
    
    for i in range(len(planilha['Planilha1'])):
        for l in range(len(planilha['Planilha1'][0])):
            texto = Label(janelaBusca, text=planilha['Planilha1'][i][l], font=("Courier", 16, "italic"))
            texto.grid(column=l, row=3+i, padx=10, pady=10)

    janelaBusca.mainloop()
    return 