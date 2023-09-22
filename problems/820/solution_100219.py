def posLetra(frase,letra,n):
    i=0
    listaletras=[]
	
    while i < len(frase):
        if frase[i] in letra:
            listaletras+=[i]
        i+=1
        
    if len(listaletras)< n:
    	return -1
    else:
    	return listaletras[n-1]