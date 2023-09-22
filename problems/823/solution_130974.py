def faltante(lista):
    """
    Dada uma lista com N-1 inteiros, numerados de 1 a N, retorna-se
    qual numero dessa lista esta faltando
    List -> int
    """
    i = 1
    list.sort(lista)
    while i<len(lista) and lista[i] - lista[i-1] == 1:
        i = i + 1
        if lista[0] != 1:
            i = 0
    return i+1