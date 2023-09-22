def posLetra(string,letra,numero):
    lista=[]
    i=0
    if str.count(string,letra)<numero:
        return -1
    while i<len(string):
        if string[i]==letra:
            list.append(lista,i)
        i=i+1
    return lista[numero-1]