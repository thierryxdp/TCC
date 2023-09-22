def repetidos(lista):
    """Função que recebe como entrada uma lista de números, e retorne o nº
    de vezes que um elemento da lista ́e igual ao elemento anterior;
    list -> int"""
    indice = 0
    contador = 0
    repete = 0
    while contador < len(lista):
        if lista[indice] == lista[indice - 1]:
            repete += 1

        indice += 1
        contador += 1

    return repete