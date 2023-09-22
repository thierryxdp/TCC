def filtraMultiplos(lista:list, n:int)->list:
    i=0
    retorno =[]	
    while i <len(lista):
        if lista[i] % n == 0:
            retorno.append(lista[i])
		i+=1
	return retorno