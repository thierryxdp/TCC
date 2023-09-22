def repetidos(lista):
    """função que retorna a quantas vezes um elemento da lista é igual ao elemento anterior
    list -> int"""
    indice = 0
    num = 0
    while indice + 1 < len(lista):
        if lista[indice] == lista[indice + 1]:
            num += 1
        indice += 1
    return num