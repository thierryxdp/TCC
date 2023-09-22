def posLetra(string,letra,ocorrencia):
    contador=0
    lista=[]
    if string.count(string,letra)<ocorrencia:
        return -1
    while contador<len(string):
        if string[contador]==letra:
            list.append(lista,contador)
            contador+=1
            return lista[ocorrencia-1]