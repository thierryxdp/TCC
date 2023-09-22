def faltante(l):
    """funcao que dada uma lista com n-1 inteiros ele retorne o numero que esta faltando.
    lista->int."""
    list.sort(l)
    i=0
    while i<len(l):
        i=i+1
        if l[0]!=l[1]-1:
    return l[0]+1