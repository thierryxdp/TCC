def repetidos(numeros):
    """Função que recebe uma lista de números, e retorna o número de vezes que um elemento da lista
    é igual ao elemento anterior; list -> int"""

    n_repetidos = 0
    indice = 0

    while (indice < len(numeros)-1):
        if numeros[indice] == numeros[indice+1]:
            n_repetidos += 1

        indice += 1

    return n_repetidos