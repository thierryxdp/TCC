def faltante(lista):
    qts = len (lista)
    n = 1
    while n <= qts:
        if n not in lista:
            return n 
        n += 1
    return