def faltante(lista):
    lista.sort()
    k = 0
    for i in lista:
        k += 1
        if i-1 != lista[k-1]:
            return i+1