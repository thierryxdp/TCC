def faltante(lista):
    """
    Dada uma lista com N-1 inteiros, numerados de 1 a N, retorna-se
    qual numero dessa lista esta faltando
    List -> int
    """
    i = 0
    list.sort(lista)
    while i<len(lista):
        if lista[0] == 1 and lista[i+1] - lista[i] != 1:
            return i+2
        if lista[0] != 1:
            return 1
        i = i + 1