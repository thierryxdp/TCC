def posLetra(frase,letra,ocorrencia):
    '''retorna a posiçao de ocorrencia da string
    str,str,int->int'''
    j=ocorrencia
    i=0
    while i<len(frase):
        if(frase.count(letra))<ocorrencia:
            return -1     
        if j==ocorrencia:
        	return frase.find(letra,i,len(frase))
        i=i+1
        j=ocorrencia+1