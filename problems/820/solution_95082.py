def posLetra(string,letra,numero):
    c=0
    f=[]
    while c<len(string):
        resultado = string.find(letra, c)
        if string[c]==resultado:
            list.append(f,resultado)
            return c
        c=c+1
    return f