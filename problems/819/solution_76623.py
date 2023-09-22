def filtraMultiplos(lista, x):
   
	multi = []
    for i in range(len(lista)):
        if lista[i]%x == 0:
            multi.append(lista[i])
    return multi