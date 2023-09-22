def faltante(lista):
    i = 1
    falta = 0
    n = len(lista) +1
    while i in range (0,n):
        if i not in lista:
            falta = falta + i
        i+=1
    return falta