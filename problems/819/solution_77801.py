def filtraMultiplos(lista,n):
    listamultiplos =[]
    for num in lista:
        if num%n == 0:
            listamultiplos.append(num)
    return listamultiplos