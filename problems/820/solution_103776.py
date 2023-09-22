def posLetra(string,letra,num):
    pos = string.find(letra)
    while pos >= num and num >1:
        if letra != string:
            return -1
        pos = string.find(letra,pos)
        n -=1
    return pos