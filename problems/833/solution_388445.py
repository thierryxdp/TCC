def conta_numero(numero, matriz):
    """Dado um numero inteiro e uma matriz (de qualquer tamanho) de
inteiros, retorna a quantidade de vezes que aquele número aparece
na matriz.
assinatura:
int, mat --> int
casos de teste:
conta_numero(1, [[1, 1, 1]]) == 3
conta_numero(1, [[1, 1, 1], [1, 1, 1]]) == 6
conta_numero(2, [[1, 2, 1], [1, 2, 1]]) == 2
"""
    repete = 0
    for n in matriz:
        for x in n:
            if x == numero:
                repete = repete + 1
    return repete