def posLetra(frase,letra,ocorrencia):
    '''retorna a posiçao de ocorrencia da string
    str,str,int->int'''
    
    i=0
    lista=[ ]
   	while i<len(frase):
        if frase[i]==letra:
            x=str.find(frase,letra,i)
            lista=lista+x
        i=i+1
        if len(lista)<ocorrencia:
            return -1
        else:
            return lista[ocorrencia-1]