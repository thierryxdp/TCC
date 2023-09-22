def posLetra(frase,letra,n):
    """função que retorna qual a posição 
    de uma string dada em uma frase, na 'n'(dada) ocorrencia
    str,str,int=>int"""
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