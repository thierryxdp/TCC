def filtraMultiplos(lista,N):
    listaNumerosMultipolsN=[]
    listaDeNumeros=lista[:]
    a=0
    while a<len(listaDeNumeros):
    	if listaDeNumeros[a]%N==0:
            listaNumerosMultipolsN=[listaDeNumeros[a]]+listaNumerosMultipolsN
   		a=a+1
    return listaNumerosMultipolsN