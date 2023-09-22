def posletra(frase,letra,numero):
    """ a """
    o=0
    for i in range (len(frase)):
        if 0==numero:
            return i-1
        if frase [i]==letra:
            o+=1
    if o < numero:
        return -1