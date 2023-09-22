def posLetra(frase,letra,ocorrencia):
    '''retorna a posiçao de ocorrencia da string
    str,str,int->int'''
    
    i=0
    while i<len(frase):
        if(frase.count(letra))<ocorrencia:
            return -1
        else:
            return frase.find(letra,0,len(frase))
        i=i+1
        j=ocorrencia+1