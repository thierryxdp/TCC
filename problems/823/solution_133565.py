def faltante(lista):
    lista1 = list(range(lista[-1]+1))
    lista1 = lista1[1:]
    i=0
    while lista[i] == lista1[i]:
        return i