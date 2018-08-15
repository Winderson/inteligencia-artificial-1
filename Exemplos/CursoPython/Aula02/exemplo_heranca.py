#!/usr/bin/env python

class Pessoa(object):

    def __init__(self):
        self._nome = ''
        self._idade = 0

    def imprime(self):
        nome = self._nome
        idade = self._idade
        print(f'{nome} - {idade}')

class Funcionario(Pessoa):

    def __init__(self, nome, idade):
        super().__init__()

        self._nome = nome
        self._idade = idade


def main():

    funcionario = Funcionario('Joao', 20)
    funcionario.imprime()


if __name__ == '__main__':
    main()