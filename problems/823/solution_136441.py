def faltante(lista):
    """Dada uma lista com n-1 elementos que são números inteiros
    e retorna qual número está faltando
    list->int"""
    list.sort(lista)
    i=0
    n=1
    tam=len(lista)
    while i<len(lista):
        if n in lista:
            n+=1
        elif n not in lista:
            return n
        elif tam==1:
            return 2
        i+=1