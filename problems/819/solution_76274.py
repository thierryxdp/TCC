def filtraMultiplos(lista,n):
    listafinal=[]
    for i in range(len(lista)):
        if lista[i]%n==0:
            listafinal.append(lista[i])
        else:
            continue
	return listafinal