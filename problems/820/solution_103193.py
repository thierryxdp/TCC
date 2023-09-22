def posLetra(string,letra,n):
    
    pos= string.find(letra)
    while pos>=0 and n>1:
        pos = string.find(letra, pos + n)
        return pos