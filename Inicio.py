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

    janelaIncerir.mainloop()
    return

def alt():
    planilha['Planilha1'][int(IdAltera.get())] = [IdAltera.get(), d1a.get(), d2a.get(), d3a.get(), d4a.get(), d5a.get()]

    save_data("tabela.ods", planilha)
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

    dado4Label = Label(janelaAltera,text="Digite o Dado4:", font="Arial")
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

def remov():
    planilha['Planilha1'].pop(int(IdRemove.get()))
    for i in range(len(planilha['Planilha1'])):
        planilha['Planilha1'][i][0] = i
    save_data("tabela.ods", planilha)
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

if __name__ == '__main__':

    janelaInicial = Tk()
    janelaInicial.title("BioDados")

    Incerir = Button(janelaInicial, text="Incerir Dados", command=Preenche, font=("Courier", 16, "italic"))
    Incerir.grid(column=0, row=1, padx=20, pady=10)

    Alterar = Button(janelaInicial, text="Alterar Dados", command=alterar, font=("Courier", 16, "italic"))
    Alterar.grid(column=0, row=2, padx=20, pady=10)

    Remover = Button(janelaInicial, text="Remover Dados", command=remover, font=("Courier", 16, "italic"))
    Remover.grid(column=0, row=3, padx=20, pady=10)

    Visualizar = Button(janelaInicial, text="Visualizar Dados", command=buscar, font=("Courier", 16, "italic"))
    Visualizar.grid(column=0, row=4, padx=20, pady=10)

    janelaInicial.mainloop()