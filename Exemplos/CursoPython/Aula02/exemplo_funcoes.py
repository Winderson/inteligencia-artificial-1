#!/usr/bin/env python

# SINTAXE:
#   def <nome_da_funcao>(<lista_parametros>):
#       <comandos>

def soma(a: int, b: int) -> int:
    """ Retorna a soma de dois numeros

    :param a: primeiro numero
    :param b: segundo numero
    :return: soma
    """
    return a + b


def imprime_texto():
    """Imprime um texto na tela."""

    texto = \
        """
            Duvida da luz dos astros,   
            De que o sol tenha calor,
            Duvida até da verdade,
            Mas confia em meu amor.
        """

    print(texto)


def main():
    x = soma(1, 2)
    print(x)

    imprime_texto()


if __name__ == '__main__':
    main()
