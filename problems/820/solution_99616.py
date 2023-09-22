def posLetra(frase,letra,ocorrencia):
    '''retorna a posiçao de ocorrencia da string
    str,str,int->int'''
    j=0
    i=0
    pos=1
    
    if(frase.count(letra))<ocorrencia:
       	return -1     
	else:
        return str.find(frase,letra,ocorrencia)