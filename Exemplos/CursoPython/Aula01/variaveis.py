#!/usr/bin/env python3

import random      # importa o namespace random
from random import randint


# Convencao python para formatacao de codigo
# PEP8 - padronizacao de codigo

# Mecanismo usado para definir que este eh o programa principal
if __name__ == '__main__':

    # Variaveis: Armazenam valores

    a = 10      # 10 eh um valor inteiro (int)
    b = 4.5     # 4.5 eh um valor float (float)
    c = 'oi'    # 'oi' eh uma string (str)
    d = True    # True/False sao valores booleanos (bool)

    # Tipos das variaveis
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))

    # Nomes de variaveis usam o snake_case
    idade_minima = 18

    # Listas
    lista1 = []  # lista vazia
    lista2 = [1, 2, 3, 4, 'cafe']

    lista2.append('abacate') # adiciona elemento ao final da lista
    lista2.insert(0, 4.16)   # insere em qualquer posicao
    lista2.pop(1)            # remove um elemento

    print(lista2)
    lista1 = lista2     # as duas listas apontam pra mesma regiao de memoria

    # Percorrendo uma lista
    for item in lista1:
        print(item)

    # Inicializacao de uma lista inline
    lista3 = []
    for i in range(1, 10):
        lista3.append(randint(10, 100))
    lista3.sort()
    print(lista3)

    lista4 = [randint(10, 100) for i in range(1, 10)]
    lista4.sort()
    print(lista4)

    lista5 = [0 for i in range(1, 10)]
    print(lista5)

    lista6 = [i for i in range(1, 10)]
    print(lista6)

    # Slice: operador para cortar a lista
    print('Exemplos de slice')

    print(lista6[5])    # retorna o elemento da posicao 5
    print(lista6[:5])   # sublista ate a posicao 5
    print(lista6[5:])   # sublista depois da posicao 5
    print(lista6[5:7])  # sublista da posicao 5 ate a 7

    print(lista6[-1])   # Indices negativos acessam a partir do final da lista
    print(len(lista6))  # A funcao len() retorna o tamanho de uma colecao

    # Tuplas
    # Colecao de coisas imutavel
    tupla1 = (1, 2, 3, 4, 'abacate')
    print(tupla1)

    # Dicionarios (mapas)
    dicionario1 = {
        'nome': 'Fred Flintstones',
        'idade': 40,
        'peso': 90.85,
        1: 'oi',
    }

    dicionario1[2] = 'abacaxi'

    print(dicionario1[1])
    print(dicionario1[2])

    print(dicionario1['nome'])
    print(dicionario1['peso'])



