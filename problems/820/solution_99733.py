def posLetra(frase,letra,ocorrencia):
    '''retorna a posiçao de ocorrencia da string
    str,str,int->int'''
    
    i=0
    lista=[ ]
	
    while i<len(frase):
        if letra==frase[i]:
            lista+=[i,]
            
   		return lista[ocorrencia-1]