def freq_palavras(string):
    lista ={}
    string=string.split()
    for i in range(len(string)):
        if string[i] in lista:
            lista[string[i]]+=1
        if string[i] not in lista:
            lista[string[i]]=1
    return lista