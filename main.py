import numpy as np
import matplotlib as plt
from pathlib import Path

def comma_to_dot(file_path):
    for a in range(3):
        with open(file_path[a], 'r+') as f:
            text = f.read()
            f.seek(0)
            f.truncate()
            f.write(text.replace(',', '.'))  

def load_files(receptora, tr):
     
     data_receptora = [np.genfromtxt(path) for path in receptora]
     data_tr = [np.genfromtxt(path) for path in tr]

     return data_receptora, data_tr


def calc_Lnt(data_receptora, data_Tr):
    
    L2 = np.array([data_receptora[i][9:25, 4] for i in range(10)])      #Carregando NPS Sala receptora
    Tr = np.array(data_Tr[0][1:-2])        #Carregando valores de T30 para as bandas de terça de 100Hz a 3.15 kHz
    To = 0.5 # Segundos, tempo de referência
    Lnt = L2 - (10*np.log10(Tr/To)) 
    
    return L2, Tr, Lnt

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
path_tr = [Path(root/'TR'/f'P{i}_TR.txt') for i in range(1,4)]
path_recept = [Path(root/f'Med{i}'/f'{i}t.txt') for i in range (1,11)]

comma_to_dot(path_tr)

d_emi, d_tr = load_files(path_recept,path_tr)

L2, Tr, Lnt = calc_Lnt(d_emi, d_tr)

# Lnt = Lnt_calc(d_emi,d_rece, d_tr)

