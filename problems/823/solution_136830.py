def faltante(lista):
    lista = lista.sort()
    i = 1
    n = 0
    dif = lista[n+1] - lista[n]
    while dif == 1:
        i+=1
        n += 1
    return i