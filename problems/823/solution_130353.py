def faltante(l):
    """funcao que dada uma lista com n-1 inteiros ele retorne o numero que esta faltando.
    lista->int."""
    list.sort(l)
    i=0
    while i<len(l)+1:
        if l[i]==l[i+1]+1:
            i=i+1
            return l[i]+1