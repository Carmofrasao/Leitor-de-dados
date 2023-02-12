# pip install pyexcel-ods3
from pyexcel_ods3 import get_data, save_data

from tkinter import *

# para gerar o executavel (tentarei deixar ele pronto, mas nunca se sabe):
# talvez precise instalar o conda
# https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
# bash ~/Downloads/Anaconda3-2022.10-Linux-x86_64.sh
# conda install -c conda-forge pyinstaller
# pyinstaller --onefile -w Inicio.py

planilha = get_data("tabela.ods")

def insere():

    dado = [d0, d1.get(), d2.get(), d3.get(), d4.get(), d5.get()]
    planilha['Planilha1'] = planilha['Planilha1'] + [dado]
    save_data("tabela.ods", planilha)
    janelaIncerir.destroy()
    return

def Preenche():

    global janelaIncerir
    janelaIncerir = Tk()
    janelaIncerir.title("BioDados")

    global d0
    d0 = len(planilha['Planilha1'])

    dado1Label = Label(janelaIncerir,text="Digite o Dado1:", font="Arial")
    dado1Label.grid(column=0, row=0, padx=10, pady=10)

    global d1
    d1 = Entry(janelaIncerir)
    d1["width"] = 25
    d1["font"] = "Arial"
    d1.grid(column=1, row=0, padx=10, pady=10)

    dado2Label = Label(janelaIncerir,text="Digite o Dado2:", font="Arial")
    dado2Label.grid(column=0, row=1, padx=10, pady=10)

    global d2
    d2 = Entry(janelaIncerir)
    d2["width"] = 25
    d2["font"] = "Arial"
    d2.grid(column=1, row=1, padx=10, pady=10)

    dado3Label = Label(janelaIncerir,text="Digite o Dado3:", font="Arial")
    dado3Label.grid(column=0, row=2, padx=10, pady=10)

    global d3
    d3 = Entry(janelaIncerir)
    d3["width"] = 25
    d3["font"] = "Arial"
    d3.grid(column=1, row=2, padx=10, pady=10)

    dado4Label = Label(janelaIncerir,text="Digite o Dado4:", font="Arial")
    dado4Label.grid(column=0, row=3, padx=10, pady=10)

    global d4
    d4 = Entry(janelaIncerir)
    d4["width"] = 25
    d4["font"] = "Arial"
    d4.grid(column=1, row=3, padx=10, pady=10)

    dado5Label = Label(janelaIncerir,text="Digite o Dado5:", font="Arial")
    dado5Label.grid(column=0, row=4, padx=10, pady=10)

    global d5
    d5 = Entry(janelaIncerir)
    d5["width"] = 25
    d5["font"] = "Arial"
    d5.grid(column=1, row=4, padx=10, pady=10)

    Inc = Button(janelaIncerir, text="Incerir", command=insere)
    Inc.grid(column=0, row=5, padx=10, pady=10)

    janelaIncerir.mainloop()
    return

def alterar():
    janelaAlterar = Tk()
    janelaAlterar.title("BioDados")

    janelaAlterar.mainloop()
    return

def remover():
    janelaRemover = Tk()
    janelaRemover.title("BioDados")

    janelaRemover.mainloop()
    return

def visualizar():
    janelaVisu = Tk()
    janelaVisu.title("BioDados")
    cabecalho = Label(janelaVisu, text=planilha['Planilha1'][0])
    cabecalho.grid(column=0, row=0, padx=10, pady=10)
    texto = Label(janelaVisu, text=planilha['Planilha1'][int(Id.get())])
    texto.grid(column=0, row=1, padx=10, pady=10)
    janelaVisu.mainloop()
    return

def buscar():
    janelaBusca = Tk()
    janelaBusca.title("BioDados")

    IdLabel = Label(janelaBusca,text="Digite o Id:", font="Arial")
    IdLabel.pack(side=TOP)
    global Id
    Id = Entry(janelaBusca)
    Id["width"] = 25
    Id["font"] = "Arial"
    Id.pack(side=LEFT)
    
    Visu = Button(janelaBusca, text="visualizar", command=visualizar)
    Visu.pack(side=BOTTOM)

    janelaBusca.mainloop()
    return 

if __name__ == '__main__':

    janelaInicial = Tk()
    janelaInicial.title("BioDados")

    Incerir = Button(janelaInicial, text="Incerir Dados", command=Preenche)
    Incerir.grid(column=0, row=1, padx=20, pady=10)

    Alterar = Button(janelaInicial, text="Alterar Dados", command=alterar)
    Alterar.grid(column=0, row=2, padx=20, pady=10)

    Remover = Button(janelaInicial, text="Remover Dados", command=remover)
    Remover.grid(column=0, row=3, padx=20, pady=10)

    Visualizar = Button(janelaInicial, text="Visualizar Dados", command=buscar)
    Visualizar.grid(column=0, row=4, padx=20, pady=10)

    janelaInicial.mainloop()