def posLetra(frase,letra,ocorrencia):
    '''retorna a posiçao de ocorrencia da string
    str,str,int->int'''
    
    i=0
    while i<len(frase):
        if(frase.count(letra))<ocorrencia:
            return -1
        else:
            return frase.find(letra,14,16)
        i=i+1