def faltante(lista)
    """Função que dado uma lista(lista) retorna qual número deste intervalo
    está faltando
    lista -> int"""

    indice = 1

    if len(lista) == 1:
        if lista[0] == 1:
            return 2
        else:
            return 1
    while indice < len(lista):
        if lista[indice] != (lista[indice-1]+1):
            return indice + 1
        indice += 1

    if lista[0] != 1:
        return 1
    else:
        return i+1