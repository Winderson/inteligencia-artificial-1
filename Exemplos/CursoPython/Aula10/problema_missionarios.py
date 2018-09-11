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

        def copy(self):
            estado = ProblemaMissionario.Estado()
            estado.margem_dir = self.margem_dir.copy()
            estado.margem_esq = self.margem_esq.copy()
            estado.barco = self.barco
            return estado

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
        return len(estado.margem_dir) == 6

    def funcao_sucessora(self, estado):
        """Gera os estados sucessores a partir de um estado."""

        # Acoes possiveis:
        # - 2 missionarios no barco
        # - 2 canibais no barco
        # - 1 missionario no barco
        # - 1 canibal no barco
        # - 1 missionario e 1 canibal no barco

        if estado.barco == DIR:

            
            novo_estado = estado.copy()
            novo_estado.margem_dir.remove(M)
            novo_estado.margem_dir.remove(M)
            novo_estado.margem_esq.append(M)
            novo_estado.margem_esq.append(M)

            print(novo_estado.margem_esq.count(M))
            print(novo_estado.margem_esq.count(C))

            print(novo_estado.margem_esq)
            print(novo_estado.margem_esq.count(M))
            print(novo_estado.margem_esq.count(C))

            print(novo_estado.margem_dir)
            print(novo_estado.margem_dir.count(M))
            print(novo_estado.margem_dir.count(C))





p = ProblemaMissionario()

p.funcao_sucessora(p.estado_inicial)
