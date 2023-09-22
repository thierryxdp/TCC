def filtraMultiplos(listaDeNumeros,N):
    listaNumerosMultipolsN=[]
    a=0
    while a<len(listaDeNumeros):
    	if listaDeNumeros[a]%N==0:
            listaNumerosMultipolsN=[listaDeNumeros[a]]+listaNumerosMultipolsN
   		a=a+1
    return listaNumerosMultipolsN