def repetidos (lista):
    """Função que dado uma lista(lista) retorne o número de vezes que um
    elemento da lista é igual ao elemento anterior.
    lista -> int"""
    indice = 0
    contador = 0
    while indice < len(lista):
        if lista[indice] == lista[indice-1]:
            contador += 1

        if indice == 0:
            contador = 0
        indice += 1

    return contador