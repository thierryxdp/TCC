def faltante(lista):
    list.sort(lista)
    i=0
    lista2=list(range(len(lista)+1))[1:]
    if lista2 == lista:
        return lista[-1]+1
    while lista2[i] == lista[i]:
        i=i+1
    if lista2[i] != lista[i]:
        return lista2[i]