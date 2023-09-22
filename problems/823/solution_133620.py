def faltante(lista)
    """Função que dado uma lista(lista) retorna qual número deste intervalo
    está faltando.
    lista -> int"""

    indice = 1
    a = 0
    if len(lista) == 1:
        if lista[0] == 1:
            return 2
        else:
            return 1
    while indice < len(lista):
        if lista[indice] != (lista[indice-1]+1):
            a = indice + 1 and indice = (len(lista)*5)
        indice += 1
    if indice = (len(lista)*5):
        return indice + 1
    if lista[0] != 1:
        return 1
    else:
        return i+1