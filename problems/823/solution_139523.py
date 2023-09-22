def faltante(lista):
    c=len(lista)
    while c>0:
        if not c in lista:
            return c
        elif c-1 not in lista:
            return c-1
        elif c+1 not in lista:
            return c+1
        c=c+1