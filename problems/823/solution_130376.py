def faltante(l):
    """funcao que dada uma lista com n-1 inteiros ele retorne o numero que esta faltando.
    lista->int."""
    lista=list(range(1,len(l)+1))
    i=0
    if l==lista:
        return len(l)+1
    elif l[0]!=1:
        return 1
    else:
        while i<len(l)+1:
        if l[i]!=l[i]+1:
            i=i+1
            return l[i]+1