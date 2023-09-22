def faltante(lista):
    """Dada uma lista com n-1 elementos que são números inteiros
    e retorna qual número está faltando
    list->int"""
    list.sort(lista)
    i=0
    n=1
    tam=len(lista)
    f=lista[-1]
    while i<len(lista):
        if n in lista:
            n+=1
        elif n not in lista:
            return n
        i=i+1
    if i==len(lista):
        return lista[-1]+1