def faltante(lista):
    i = 1
    n = len(lista) +1
    while i < n:
        if i not in range(1,n):
             falta = i
        i+=1
    return falta