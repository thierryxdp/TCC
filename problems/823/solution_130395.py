def faltante(l):
    """funcao que dada uma lista com n-1 inteiros ele retorne o numero que esta faltando.
    lista->int."""
    p=len(l)+1
    i=0
    while i<p:
        if i+1 not in l:
            return i+1
        if l[i] != i+1:
            return i+1
        else:
            i=i+1