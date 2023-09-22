def repetidos(lista_numeros):
    """Recebe uma lista de números e informa quantas vezes
    os valores foram iguais aos que vieram anteriormente.
    list -> int"""
    indice = 0
    repeticoes = 0
    while indice < len(lista_numeros):
        if lista_numeros[indice] == lista_numeros[indice+1]:
            repeticoes += 1
        indice += 1
    return repeticoes