#!/usr/bin/env python
from pprint import pprint
from typing import List

from Aula10.problema import Problema


class BuscaSemInformacao(object):

    def busca_largura(self, problema: Problema):
        """Agente que implementa a busca em largura

        :param problema: definicao do problema
        :return: lista com os estados para chegar na solucao do problema
        """

        # 1. Adiciona o estado inicial na lista de borda
        borda = [problema.estado_inicial]

        while True:

            # 2. Verifica se houve falha
            if not borda:
                print('Falha ao encontrar solucao')
                return []

            # 3. Recupera o proximo estado
            estado = borda.pop(0)
            print(estado)
            print(type(estado))

            # 4. Verifica se achou a solucao objetivo
            if problema.funcao_objetivo(estado):
                print('Solucao encontrada.')
                return problema.solucao(estado)

            # 5. Geracao dos estados sucessores
            # ** Na busca em largura, os estados sucessores sao adicionados
            # ** ao final da lista
            borda.append(problema.funcao_sucessora(estado))


