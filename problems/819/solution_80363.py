def filtraMultiplos(lista,n):
    ''''''
    i=0
    lista = []
    listanova = []
    while i<len(lista):
        if lista[i]%n == 0:
            listanova=listanova+lista[i]
        i=i+1
    return listanova