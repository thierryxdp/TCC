def filtraMultiplos(listaDeNumeros,N):
    list.listaNumerosMultipolsN=[]
    i=0
    while i<len(listaDeNumeros):
    	if list.listaDeNumeros[i]%N==0:
    		list.listaNumerosMultipolsN=list.listaDeNumeros[i]+list.listaNumerosMultipolsN
    	i=i+1
    return listaNumerosMultipolsN