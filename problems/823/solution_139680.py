def faltante(lista):
    i = 1
    n = len(lista) +1
    while i < len(lista):
        if i not in range(1,n):
            x = i
        i+=1
    return x