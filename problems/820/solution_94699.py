def posLetra(texto,letra,num_ocorrencia):
    indice=0
    lista=[]
    if texto.count(letra)<num_ocorrencia:
        return -1
    while indice<len(texto):
        if texto[indice] == letra:
            lista+=[indice]
        indice+=1
    return lista[num_ocorrencia-1]