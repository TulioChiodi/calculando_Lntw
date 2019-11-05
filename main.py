import numpy as np
import matplotlib as plt
from pathlib import Path

def load_files(emissor, tr):
     
     lista_emissor = [np.genfromtxt(path) for path in emissor]
     data_tr = np.genfromtxt(tr)

     return lista_emissor, data_tr


#def Lnt_calc(data_emissor, data_tr):
#
#
#
#     return Dnt


def nearest_32():



     return


def unique_value_500Hz():



     return


def soma_das_diferencas():



     return


def plotting():
     pass


root = Path('./medicoes')
path_tr = Path(root/'TR.xlsx')
path_emi = [Path(root/f'Med{i}'/f'{i}t.txt') for i in range (1,11)]

d_emi, d_tr = load_files(path_emi,path_tr)
# Lnt = Lnt_calc(d_emi,d_rece, d_tr)

