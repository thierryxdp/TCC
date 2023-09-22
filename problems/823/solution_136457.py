def faltante(lista):
    """Dada uma lista com n-1 elementos que são números inteiros
    e retorna qual número está faltando
    list->int"""
    list.sort(lista)
    i=0
    n=1
    tam=len(lista)
    numero=tam+1
    while i<lista[i]:
        if n in lista:
            n+=1
        elif n not in lista:
            return n
        elif n==lista(-1):
            return lista(-1)+1
        i=i+1