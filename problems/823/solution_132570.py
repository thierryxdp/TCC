def faltante(lista):
    list.sort(lista)
    i=0
    listafinal=list(range(len(lista)+1))[1:]
    if listafinal == lista:
        return lista[-1]+1
    while listafinal[i] == lista[i]:
        i=i+1
    if listafinal[i] != lista[i]:
        return listafinal[i]