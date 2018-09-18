#!/usr/bin/env python
from pprint import pprint

from Aula10.busca_sem_informacao import BuscaSemInformacao
from Aula10.problema_missionarios import ProblemaMissionario
from Aula10.problema import Problema


def main():
    # Definicao do problema dos canibais
    problema = ProblemaMissionario()

    busca = BuscaSemInformacao()
    solucao = busca.busca_largura(problema)

    pprint(solucao)


if __name__ == '__main__':
    main()