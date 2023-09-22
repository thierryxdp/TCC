def posLetra(frase,letra,ocorrencia):
    '''retorna a posiçao de ocorrencia da string
    str,str,int->int'''
    
    i=0
    lista=[ ]
	
    if len(lista)<ocorrencia:
   		return -1while i<len(frase):

    while i<len(frase):
    	if letra==frase[i]:
        	lista+=[i,]
        i=i+1
	return lista[ocorrencia-1]