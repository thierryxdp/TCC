def faltante(lista):
    c=len(lista) + 1
    while c>0:
        if c not in lista:
            return c
        c=c+1