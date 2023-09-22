def faltante(lista):
    lista.sort()
    n = 1
    for i in lista:
        if i != n:
            return n
        n+=1
    return i + 1