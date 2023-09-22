def posLetra(frase,letra,ocorrencia):
    i=0
    lista=[]
    if ocorrencia<=frase.count(letra):
        while i< len(frase):
            if frase[i] in letra:
                list.append(lista,i)
            i+=1
        return lista[ocorrencia-1]
    else:
        return -1