def faltante(lista):
    """funcao que dada uma lista com n inteiros de 1 a n, descobre qual numero
    está faltando na lista. list->int"""
    i=1
    n= 0
    list.append(lista,0)
    while i<len(lista):
        if i !=lista[n]:
            return i
        i=i+1
        n=n+1
    return i