def faltante(lista):
    c=len(lista)
    while c>0:
        if not c in lista:
            return c
        c=c+1