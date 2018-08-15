#!/usr/bin/env python

import pandas as pd

# instalar: pandas xwlr xlrd

def main():

    dados = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
    ]
    colunas = ['um', 'dois', 'tres', 'quatro', 'cinco']

    # DataFrame: Classe que representa os tabelados
    df1 = pd.DataFrame(dados, columns=colunas)
    print(df1)

    df2 = pd.read_csv('dataset.csv', sep=';')
    print(df2)

    df3 = pd.read_excel('notas.xls')
    df3.to_excel('notas_new.xls')
    print(df3)

    for indice, row in df3.iterrows():
        #print(indice)
        #print(row)
        nome = row['nome']
        media = (row['nota1'] + row['nota2']) / 2
        print(f'{nome:10s}: {media}')







if __name__ == '__main__':
    main()