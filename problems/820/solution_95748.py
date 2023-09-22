def posLetra(string,letra,numero):
    i=0
    while i<len(string):
        contador=contador+str.index(string,letra)
        str.find(string,letra,contador)
        if numero>str.count(string,letra):
            return -1
        i=i+1
    return str.index(string,letra)