def posLetra(frase,letra,ocorrencia):
    '''retorna a posiçao de ocorrencia da string
    str,str,int->int'''
    
    i=0
    lista=[]
    while i<len(frase):
        if frase[i]==letra:
            x=str.find(frase,letra,ocorrencia)
            lista=lista+[frase[i]]
        i=i+1
        if ocorrencia>len(lista):
            return -1
        else:
            return lista[ocorrencia-1]