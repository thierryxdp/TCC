def posLetra(frase,letra,ocorrencia):
    '''retorna a posiçao de ocorrencia da string
    str,str,int->int'''
    j=0
    i=0
    pos=0
    
    if(frase.count(letra))<ocorrencia:
       	return -1     
    while i<len(frase):
        if j==ocorrencia:
        	return frase.find(letra,(pos),)
        else: 
        	i=frase.find(letra,(pos),)
            j+=1