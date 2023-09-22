def faltante(lista):
    """Dada uma lista com n-1 elementos que são números inteiros
    e retorna qual número está faltando
    list->int"""
    list.sort(lista)
    i=0
    n=0
    tam=len(lista)
    numero=tam+1
    while i<len(lista):
        if n in lista:
            n+=1
        elif n not in lista and n!=0:
            return n
        elif i==tam:
            return numero
        i=i+1