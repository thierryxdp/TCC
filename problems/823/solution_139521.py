def faltante(lista):
    c=len(lista) + 1
    while c>0:
        if not c in lista:
            return c
        c=c+1