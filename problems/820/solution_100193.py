def posLetra(frase,letra,n):
    i=0
    listaletras=[]
	
    while i < len(frase):
        if frase[i] == letra:
            listaletras+=[str.index(frase,frase[i])]
        i+=1
        
    if len(listaletras)< n:
    	return -1
    else:
    return listaletras[n-1]