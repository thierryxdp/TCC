def posLetra(frase,letra,ocorrencia):
    '''retorna a posiçao de ocorrencia da string
    str,str,int->int'''
    
    i=0
    while i<len(frase):
        if(frase[i])==letra:
            if(frase.count(letra))<ocorrencia:
            	return -1
        	if 1==1:
            	return str.find(frase,letra,ocorrencia)
       
        i=i+1