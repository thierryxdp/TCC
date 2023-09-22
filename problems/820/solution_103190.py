def posLetra(string,letra,n):
    
    pos= string.find(letra)
    while i>=0 and n>1:
        pos = string.find(string,letra, i + n)
        return pos