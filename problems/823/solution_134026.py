def faltante(l):
    lista=l.sort()
    x=1
    while x<len(lista):
        if l[x]!=x:
            return x