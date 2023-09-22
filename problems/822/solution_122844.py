def repetidos(lista):
    """Ao fornecer uma lista de números, retorne o número de vezes que
    um elemento da lista é igual ao elemento anterior.

    list -> int"""

    indice = 0
    contador = 0

    while indice < len(lista):
        if lista[indice] == lista[indice-1]:
            contador += 1

        indice += 1

    return contador