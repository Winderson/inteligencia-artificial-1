#!/usr/bin/env python

# SINTAXE:
#   class <NomeDaClasse>(<classe_pai>):
#       <metodos>
from typing import List

import numpy as np


class Aluno():
    """Representa um aluno da escola."""

    def __init__(self, nome:str = ''):
        """Construtor da classe."""

        # No construtor sao declarados os atributos

        # Atributos sao sempre publicos
        # self.nome = nome
        # self.sobrenome = ''
        # self.notas = [0, 0]

        # Atributos protegidos
        # self._nome = nome
        # self._sobrenome = ''
        # self._notas = []

        # Atributos privados
        self.__nome = nome.upper()
        self.__sobrenome = ''
        self.__notas = []

    def __str__(self):
        texto = ''
        texto += f'Nome.....: {self.__nome} {self.__sobrenome}\n'
        texto += f'Notas....: {self.__notas}\n'
        texto += f'Media....: {self.media()}\n'
        return texto

    def __lt__(self, other):
        return self.media() < other.media()

    # @property: decorator - Injeta codigo em alguma funcao
    # Usado para gerar um getter
    @property
    def nome(self):
        return self.__nome.upper()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def sobrenome(self):
        return self.__sobrenome.upper()

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    @property
    def notas(self):
        return self.__notas

    @notas.setter
    def notas(self, notas: List[float]):

        for nota in notas:
            if nota < 0 or nota > 100:
                raise RuntimeError('Nota fora do intervalo 0..100')

        self.__notas = notas

    def media(self):
        return np.mean(self.__notas)


def main():

    aluno1 = Aluno()
    aluno1.nome = 'Joaquim'
    aluno1.sobrenome = 'Branganca e Orleans'
    aluno1.notas = [90, 100]

    aluno2 = Aluno('Carlinhos')
    aluno2.notas = [20, 90]


    aluno3 = Aluno(nome='Chiquinha')

    print(f'Nome.....: {aluno1.nome} {aluno1.sobrenome}')
    print(f'Notas....: {aluno1.notas}')
    print(f'Media....: {aluno1.media()}')

    print(aluno2)





if __name__ == '__main__':
    main()