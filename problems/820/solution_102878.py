def posLetra(frase,letra,ocorrencia):
    i=0
    lista=[]
    while i<len(frase):
        if frase[i]==letra:
            lista=+[i]
        i+=1
            
    if ocorrencia>len(lista):
        return -1
    else:
        return lista[ocorrencia-1]