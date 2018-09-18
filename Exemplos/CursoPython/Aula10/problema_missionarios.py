#!/usr/bin/env python
from enum import Enum

from Aula10.problema import Problema

# Constantes para o problema dos missionarios e canibais
M = 'missionario'
C = 'canibal'
D = 'direita'
E = 'esquerda'

ESQ = 0
DIR = 1


class ProblemaMissionario(Problema):
    """Definicao do problema de missionarios e canibais."""

    class Estado(object):
        """Modelagem de um estado do problema."""

        def __init__(self):
            self.margem_dir = []
            self.margem_esq = []
            self.barco = 0

            # Referencia para o estado pai. Usado para descobrir qual eh
            # a solucao do problema
            self.pai = None
            self.custo = 0
            self.acao = ''

        def copy(self):
            estado = ProblemaMissionario.Estado()
            estado.margem_dir = self.margem_dir.copy()
            estado.margem_esq = self.margem_esq.copy()
            estado.barco = self.barco
            return estado

        def __repr__(self):
            return f'{self.margem_esq} | {self.barco} | {self.margem_dir}'

    @property
    def estado_inicial(self):
        """Retorna o estado inicial do problema."""
        estado = ProblemaMissionario.Estado()

        # Todos estao na margem direita do rio
        estado.margem_esq = []
        estado.margem_dir = [M, M, M, C, C, C]
        estado.barco = DIR
        estado.pai = None

        return estado

    def solucao(self, estado):
        """Gera uma lista com a solucao de um problema a partir de um estado."""

        # Percorre toda a lista de estados ate o estado inicial
        solucao_final = []
        while estado.pai is not None:
            solucao_final.append(estado)
            estado = estado.pai

        # Inclui o estado inicial na lista
        solucao_final.append(estado)

        # Retorna a solucao
        return solucao_final.reverse()

    def funcao_objetivo(self, estado):
        """Verifica se a funcao atingiu o seu objetivo."""

        # Todos estao do lado esquerdo do rio
        return len(estado.margem_esq) == 6

    def __mover_para_esq(self, estado_pai, pessoas, acao):
        """Move pessoas para a margem esquerda."""
        estado = estado_pai.copy()

        # Salva a acao ja realizada
        estado.acao = acao

        # Remove da margem direita
        for p in pessoas:
            if p not in estado.margem_dir:
                return None
            estado.margem_dir.remove(p)

        # Move o barco
        estado.barco = ESQ

        # Desembarca na margem esquerda
        for p in pessoas:
            if p not in estado.margem_esq:
                return None
            estado.margem_esq.append(p)

        # Define o no pai do estado atual
        estado.pai = estado_pai

        # Verifica se o estado eh valido
        return self.__valida_restricoes(estado)

    def __mover_para_dir(self, estado_pai, pessoas, acao):
        """Move pessoas para a margem direita."""
        estado = estado_pai.copy()

        # Salva a acao ja realizada
        estado.acao = acao

        # Remove da margem esquerda
        for p in pessoas:
            if p not in estado.margem_esq:
                return None
            estado.margem_esq.remove(p)

        # Move o barco
        estado.barco = DIR

        # Desembarca na margem esquerda
        for p in pessoas:
            if p not in estado.margem_dir:
                return None
            estado.margem_dir.append(p)

        # Define o no pai do estado atual
        estado.pai = estado_pai

        # Verifica se o estado eh valido
        return self.__valida_restricoes(estado)

    def __valida_restricoes(self, estado):

        # 1. Numero total de canibais e missionarios deve ser 6
        print(estado)

        total_m = estado.margem_esq.count(M) + estado.margem_dir.count(M)
        total_c = estado.margem_esq.count(C) + estado.margem_dir.count(C)
        print(total_m)
        print(total_c)

        # 2. Verifica restricao de missionarios >= canibais e missionarios
        diferenca_esq = estado.margem_esq.count(M) - estado.margem_esq.count(C) if estado.margem_esq.count(
            M) != 0 else 0
        diferenca_dir = estado.margem_dir.count(M) - estado.margem_dir.count(C) if estado.margem_dir.count(
            C) != 0 else 0
        print(diferenca_esq)
        print(diferenca_dir)

        print('-' * 3)

        # Retorna o estado caso ele seja valido
        if total_m == 3 and total_c == 3 and diferenca_esq >= 0 and diferenca_dir >= 0:
            return estado
        else:
            return None

    def funcao_sucessora(self, estado):
        """Gera os estados sucessores a partir de um estado."""

        # Acoes possiveis:
        # - 2 missionarios no barco
        # - 2 canibais no barco
        # - 1 missionario no barco
        # - 1 canibal no barco
        # - 1 missionario e 1 canibal no barco
        sucessores = []

        if estado.barco == DIR:
            print('Movendo barco para esquerda')
            a1 = self.__mover_para_esq(estado, [M, M], '2M')
            a2 = self.__mover_para_esq(estado, [C, C], '2C')
            a3 = self.__mover_para_esq(estado, [M], '1M')
            a4 = self.__mover_para_esq(estado, [C], '1C')
            a5 = self.__mover_para_esq(estado, [M, C],'1M 1C')
        else:
            a1 = self.__mover_para_dir(estado, [M, M], '2M')
            a2 = self.__mover_para_dir(estado, [C, C], '2C')
            a3 = self.__mover_para_dir(estado, [M], 'M')
            a4 = self.__mover_para_dir(estado, [C], 'C')
            a5 = self.__mover_para_dir(estado, [M, C], '1M 1C')

        # Cria uma lista apenas com os estados validos
        if a1: sucessores.append(a1)
        if a2: sucessores.append(a2)
        if a3: sucessores.append(a3)
        if a4: sucessores.append(a4)
        if a5: sucessores.append(a5)

        return sucessores

