def repetidos(lista):
    """função que recebe uma lista de números e retorna o
    número de vezes que um elemento da lista é igual ao
    elemento anterior.
    list -> int"""

    i = 1
    contador = 0

    while i < len(lista):
        if lista[i] == lista[i-1]:
            contador += 1
        i += 1
    return contador