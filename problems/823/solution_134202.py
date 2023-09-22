def faltante(lista):
    """essa função recebe uma lista contendo uma sequência de 
    N - 1 inteiros não repetidos numerados de 1 a n e retorna 
    o valor que está faltando na lista;
    list->int"""
    list.reverse(lista)
    num = lista[0]
    list.sort(lista)
    i = 0
    a = 0
    while i < num:
        a = a + 1
        if a != lista[i]:
            return a
        i = i + 1
    return i + 1