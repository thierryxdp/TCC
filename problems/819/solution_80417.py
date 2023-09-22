def filtraMultiplos(listaDeNumeros,N):
    listaNumerosMultipolsN=[]
    i=0
    while i<len(listaDeNumeros):
    	if listaDeNumeros[i]%N==0:
    		listaNumerosMultipolsN=list.append(listaNumerosMultipolsN,listaDeNumeros[i])
    	i=i+1
    return listaNumerosMultipolsN