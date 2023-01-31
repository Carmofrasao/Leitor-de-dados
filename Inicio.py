# pip install pyexcel-ods3
from pyexcel_ods3 import get_data, save_data

from tkinter import *

planilha = get_data("tabela.ods")

def incere():

    dado = [d0, d1.get(), d2.get(), d3.get(), d4.get(), d5.get()]
    planilha['Planilha1'] = planilha['Planilha1'] + [dado]
    save_data("tabela.ods", planilha)
    return

def Preenche():

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

    Inc = Button(janelaIncerir, text="Incerir", command=incere)
    Inc.grid(column=0, row=5, padx=10, pady=10)

    janelaIncerir.mainloop()
    return

def alt():
    planilha['Planilha1'][int(IdAltera.get())][1] = d1a.get()
    planilha['Planilha1'][int(IdAltera.get())][2] = d2a.get()
    planilha['Planilha1'][int(IdAltera.get())][3] = d3a.get()
    planilha['Planilha1'][int(IdAltera.get())][4] = d4a.get()
    planilha['Planilha1'][int(IdAltera.get())][5] = d5a.get()
    save_data("tabela.ods", planilha)

def altera():
    janelaAltera = Tk()
    janelaAltera.title("BioDados")

    dado1Label = Label(janelaAltera,text="Digite o Dado1:", font="Arial")
    dado1Label.grid(column=0, row=0, padx=10, pady=10)

    global d1a
    d1a = Entry(janelaAltera)
    d1a.insert(0, planilha['Planilha1'][int(IdAltera.get())][1])
    d1a["width"] = 25
    d1a["font"] = "Arial"
    d1a.grid(column=1, row=0, padx=10, pady=10)

    dado2Label = Label(janelaAltera,text="Digite o Dado2:", font="Arial")
    dado2Label.grid(column=0, row=1, padx=10, pady=10)

    global d2a
    d2a = Entry(janelaAltera)
    d2a.insert(0, planilha['Planilha1'][int(IdAltera.get())][2])
    d2a["width"] = 25
    d2a["font"] = "Arial"
    d2a.grid(column=1, row=1, padx=10, pady=10)

    dado3Label = Label(janelaAltera,text="Digite o Dado3:", font="Arial")
    dado3Label.grid(column=0, row=2, padx=10, pady=10)

    global d3a
    d3a = Entry(janelaAltera)
    d3a.insert(0, planilha['Planilha1'][int(IdAltera.get())][3])
    d3a["width"] = 25
    d3a["font"] = "Arial"
    d3a.grid(column=1, row=2, padx=10, pady=10)

    dado4Label = Label(janelaAltera,text="Digite o Dado4:", font="Arial")
    dado4Label.grid(column=0, row=3, padx=10, pady=10)

    global d4a
    d4a = Entry(janelaAltera)
    d4a.insert(0, planilha['Planilha1'][int(IdAltera.get())][4])
    d4a["width"] = 25
    d4a["font"] = "Arial"
    d4a.grid(column=1, row=3, padx=10, pady=10)

    dado5Label = Label(janelaAltera,text="Digite o Dado5:", font="Arial")
    dado5Label.grid(column=0, row=4, padx=10, pady=10)

    global d5a
    d5a = Entry(janelaAltera)
    d5a.insert(0, planilha['Planilha1'][int(IdAltera.get())][5])
    d5a["width"] = 25
    d5a["font"] = "Arial"
    d5a.grid(column=1, row=4, padx=10, pady=10)

    Inc = Button(janelaAltera, text="Alterar", command=alt)
    Inc.grid(column=0, row=5, padx=10, pady=10)

    janelaAltera.mainloop()
    return

def alterar():
    janelaAlterar = Tk()
    janelaAlterar.title("BioDados")

    IdLabel = Label(janelaAlterar,text="Digite o Id:", font="Arial")
    IdLabel.pack(side=TOP)
    global IdAltera
    IdAltera = Entry(janelaAlterar)
    IdAltera["width"] = 25
    IdAltera["font"] = "Arial"
    IdAltera.pack(side=LEFT)
    
    Remo = Button(janelaAlterar, text="Alterar", command=altera)
    Remo.pack(side=BOTTOM)

    janelaAlterar.mainloop()
    return

def remov():
    planilha['Planilha1'].pop(int(IdRemove.get()))
    save_data("tabela.ods", planilha)

def remover():
    janelaRemover = Tk()
    janelaRemover.title("BioDados")

    IdLabel = Label(janelaRemover,text="Digite o Id:", font="Arial")
    IdLabel.pack(side=TOP)
    global IdRemove
    IdRemove = Entry(janelaRemover)
    IdRemove["width"] = 25
    IdRemove["font"] = "Arial"
    IdRemove.pack(side=LEFT)
    
    Remo = Button(janelaRemover, text="Remover", command=remov)
    Remo.pack(side=BOTTOM)

    janelaRemover.mainloop()
    return

def visualizar():
    janelaVisu = Tk()
    janelaVisu.title("BioDados")
    cabecalho = Label(janelaVisu, text=planilha['Planilha1'][0])
    cabecalho.grid(column=0, row=0, padx=10, pady=10)
    texto = Label(janelaVisu, text=planilha['Planilha1'][int(IdBusca.get())])
    texto.grid(column=0, row=1, padx=10, pady=10)
    janelaVisu.mainloop()
    return

def buscar():
    janelaBusca = Tk()
    janelaBusca.title("BioDados")

    IdLabel = Label(janelaBusca,text="Digite o Id:", font="Arial")
    IdLabel.pack(side=TOP)
    global IdBusca
    IdBusca = Entry(janelaBusca)
    IdBusca["width"] = 25
    IdBusca["font"] = "Arial"
    IdBusca.pack(side=LEFT)
    
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