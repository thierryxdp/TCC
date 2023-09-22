#
#
#
#
def posLetra(string,letra,numero):
    i=0
    j=1
    posicao = int
    while i < len(string) and j <= numero:
        if string(i) == letra:
            i=i+1
            posicao = i - 1
    j=j+1    
    return posicao