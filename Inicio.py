from tkinter import Tk, Button
from Incerir import Preenche
from Alterar import alterar
from Remover import remover
from Visualizar import buscar

# pip install pyexcel-ods3
# para gerar o executavel (tentarei deixar ele pronto, mas nunca se sabe):
# talvez precise instalar o conda
# https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
# bash ~/Downloads/Anaconda3-2022.10-Linux-x86_64.sh
# conda install -c conda-forge pyinstaller
# pyinstaller --onefile -w Inicio.py

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