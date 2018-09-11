#!/usr/bin/env python
from pprint import pprint
from typing import List


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

            # 4. Verifica se achou a solucao objetivo
            if problema.funcao_objetivo(estado):
                print('Solucao encontrada.')
                return problema.solucao(estado)

            # 5. Geracao dos estados sucessores
            # ** Na busca em largura, os estados sucessores sao adicionados
            # ** ao final da lista
            borda.append(problema.funcao_sucessora(estado))


def teste_objetivo_mc(estado):
    """Verifica se encontrou o estado final do problema."""
    return estado.sort() == ([C, C, C, M, M, M], ESQ, [])

def funcao_sucessora_mc(estado):
    proximos_estados = []

    if estado[BARCO] == D:
        # Coloca duas pessoas no barco, desde que nao fiquem
        # mais canibais que missionarios

        # -------------------------------------------
        # 1. Acao: colocar dois missionarios no barco
        esq = estado[ESQ].copy()
        dir = estado[DIR].copy()

        # Moveu os missionarios
        dir.remove(M)
        dir.remove(M)
        esq.append(M)
        esq.append(M)

        num_missionarios_dir = estado[DIR].count(M)
        num_canibais_dir = estado[DIR].count(C)

        num_missionarios_esq = estado[ESQ].count(M)
        num_canibais_esq = estado[ESQ].count(C)

        # Verifica se o estado eh valido
        if num_canibais_esq <= num_missionarios_esq \
                and num_canibais_dir <= num_missionarios_dir:
            proximos_estados.append((esq, E, dir))

        # ---------------------------------------------
        # 2. Acao: colocar dois canibais no barco
        esq = estado[ESQ].copy()
        dir = estado[DIR].copy()

        # Moveu os missionarios
        dir.remove(C)
        dir.remove(C)
        esq.append(C)
        esq.append(C)

        num_missionarios_dir = estado[DIR].count(M)
        num_canibais_dir = estado[DIR].count(C)

        num_missionarios_esq = estado[ESQ].count(M)
        num_canibais_esq = estado[ESQ].count(C)

        # Verifica se o estado eh valido
        if num_canibais_esq <= num_missionarios_esq \
                and num_canibais_dir <= num_missionarios_dir:
            proximos_estados.append((esq, E, dir))

        # ---------------------------------------------
        # 3. Acao: colocar um canibal e um missionario
        esq = estado[ESQ].copy()
        dir = estado[DIR].copy()

        # Moveu os missionarios
        dir.remove(C)
        dir.remove(M)
        esq.append(C)
        esq.append(M)

        num_missionarios_dir = estado[DIR].count(M)
        num_canibais_dir = estado[DIR].count(C)

        num_missionarios_esq = estado[ESQ].count(M)
        num_canibais_esq = estado[ESQ].count(C)

        # Verifica se o estado eh valido
        if num_canibais_esq <= num_missionarios_esq \
                and num_canibais_dir <= num_missionarios_dir:
            proximos_estados.append((esq, E, dir))

        # ---------------------------------------------
        # 4. Acao: colocar um canibal
        esq = estado[ESQ].copy()
        dir = estado[DIR].copy()

        # Moveu os missionarios
        dir.remove(C)
        esq.append(C)

        num_missionarios_dir = estado[DIR].count(M)
        num_canibais_dir = estado[DIR].count(C)

        num_missionarios_esq = estado[ESQ].count(M)
        num_canibais_esq = estado[ESQ].count(C)

        # Verifica se o estado eh valido
        if num_canibais_esq <= num_missionarios_esq \
                and num_canibais_dir <= num_missionarios_dir:
            proximos_estados.append((esq, E, dir))

        # ---------------------------------------------
        # 5. Acao: colocar um missionario
        esq = estado[ESQ].copy()
        dir = estado[DIR].copy()

        # Moveu os missionarios
        dir.remove(M)
        esq.append(M)

        num_missionarios_dir = estado[DIR].count(M)
        num_canibais_dir = estado[DIR].count(C)

        num_missionarios_esq = estado[ESQ].count(M)
        num_canibais_esq = estado[ESQ].count(C)

        # Verifica se o estado eh valido
        if num_canibais_esq <= num_missionarios_esq \
                and num_canibais_dir <= num_missionarios_dir:
            proximos_estados.append((esq, E, dir))

    else:
        # Coloca duas pessoas no barco, desde que nao fiquem
        # mais canibais que missionarios
        # TODO: Implementar o lado esquerdo
        # TODO: Simplificar o metodo

        # Atravessa o barco
        #estado[BARCO] = D
        pass

    return proximos_estados

def main():

    # Definicao do problema dos canibais
    problema = {
        'estado_inicial': ([], D, [M, M, M, C, C, C]),
        'teste_objetivo': teste_objetivo_mc,
        'gerar_sucessores': funcao_sucessora_mc,
    }

    pprint(funcao_sucessora_mc(([], D, [M, M, M, C, C, C])))



if __name__ == '__main__':
    main()