def repetidos(lista_numeros):
    """recebe uma lista de numeros e diz quantas vezes um numero
    é igual ao anterior;
    lista, -> int"""
    l = lista_numeros
    x = 1
    for soma in range(len(l)):
        if l[x] == (l[x-1]):
            i = i + 1
    return soma