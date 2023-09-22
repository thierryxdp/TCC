def faltante(lista):
    lista = lista.sort()
    i = 1
    dif = lista[i+1] - lista[i]
    while dif == 1:
        i+=1
    return i