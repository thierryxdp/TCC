def posLetra(string,letra,numero):
    c=0
    f=[]
    while c<len(string):
        resultado = string.find(letra, c)
        if string[c]==resultado:
            return c
        list.append(f,c)
        c=c+1
    return -1