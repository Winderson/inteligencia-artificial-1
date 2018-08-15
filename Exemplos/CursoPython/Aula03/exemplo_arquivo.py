#!/usr/bin/env python


def main():
    """Exemplo de manipulacao de arquivos"""

    arquivo = 'texto.txt'

    # Abre o arquivo para modo leitura
    with open(arquivo, 'r') as file:
        conteudo = file.readlines()

    # Abre o arquivo para modo escrita
    with open('saida.txt', 'w') as file:
        for linha in conteudo:

            # Quebra uma string em tokens
            tokens = linha.split('.')

            for token in tokens:
                file.write(token.strip() + '\n')


if __name__ == '__main__':
    main()
