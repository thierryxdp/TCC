def posLetra(string,letra,numero):
    i=0
    lista=[]
    while i<len(string):
        if string[numero]==letra:
            lista.append(numero)
            i+=1
        else:
            i+=1
    if len(lista)==numero:
        return lista[-1]
    elif len(lista)>numero:
        return lista[n-1]
    else:
        return -1