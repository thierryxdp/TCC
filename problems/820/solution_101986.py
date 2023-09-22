def posLetra(frase,letra,n):
    """ Função que identifica a posição da ocorrencia n de uma letra, dada uma frase qualquer
    str,str,int -> int """
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