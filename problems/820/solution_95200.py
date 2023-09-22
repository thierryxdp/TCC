def posLetra (frase,string,posicao):
    if frase.count(string)<posicao:
        return - 1
    indices=[]
    i=0
    while i<len(frase):
        if frase[i]==string:
            indices.append(i)
        i+=1
    return indices[posicao-1]