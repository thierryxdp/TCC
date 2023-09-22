def faltante(lista):
    lista1 = list(range(lista[-1]))
    i=1
    while lista[i] == lista1[i]:
        i+=1
    return lista1[i]