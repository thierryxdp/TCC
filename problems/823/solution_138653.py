def faltante(lista):
    n = len(lista) + 1
    while n>0:
        if n not in lista:
            return n
        n = n - 1