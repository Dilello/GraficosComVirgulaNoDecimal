import glob
import pandas as pd

#IMPORTANTE#
#Criar uma pasta onde contenha APENAS os arquivos com dados brutos

# ler todos os arquivos da pasta: 'Caminho/*.txt'

CaminhoDadoBruto = 'Documents/Caminho/*.txt'

j = 0
for i in glob.glob(CaminhoDadoBruto, recursive = True):
    j += 1
    globals()["dado" + str(j)] = pd.read_csv(i, sep = '\s+',header = None)




