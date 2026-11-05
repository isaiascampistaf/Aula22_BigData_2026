import pandas as pd 
import polars as pl #pip install polars 
from datetime import datetime  #biblioteca p/ data e hora

ENDERECO_DADOS = './../DADOS/'

#Obtendo janeiro e fevereiro 

try:
    inicio = datetime.now()
    print('Obtendo os dados de Janeiro e Fevereiro ')
    
    lista_arquivos = ['202601_NovoBolsaFamilia.csv','202602_NovoBolsaFamilia.csv','202603_NovoBolsaFamilia.csv']

    df_bolsa_familia = None 

    for arquivo in lista_arquivos:
        df = pl.read_csv(ENDERECO_DADOS + arquivo ,separator=';',encoding='iso-8859-1')

        # print(df)  pd-34s  pl-25s


        if df_bolsa_familia is None:
            df_bolsa_familia = df 
        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia,df])

        del df # deleta o dataframe temporario 'df'

    print(df_bolsa_familia) 


    fim = datetime.now()
    print(f'Tempo total: {fim - inicio}')

except Exception as e:
    print(f'')