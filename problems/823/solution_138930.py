def faltante(l):
    lista1=l[1:]
    for e in l:
        if lista1[e]!=l[e]+1:
            return l[e]+1