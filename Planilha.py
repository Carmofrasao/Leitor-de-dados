from pyexcel_ods3 import get_data, save_data

planilha = get_data("tabela.ods")

def salva(inf):
    save_data("tabela.ods", inf)
    return