def posLetra(texto, letra, ocorrencia):
    i=0
    o=0
    ind=[]
    if o<ocorrencia:
        return -1
    while not(o==ocorrencia):
        if texto[i]==letra:
            o=o+1
            ind=texto[i]
        i=i+1
    return list.pop(ind, -1)