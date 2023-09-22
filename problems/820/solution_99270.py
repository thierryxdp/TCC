#
#
#
#
def posLetra(string,letra,numero):
    i=0
    j=1
    posicao = 0
    while i < len(string) and j <= numero:
        if string[i]==letra:
            posicao = posicao + 1
    i=i+1       
    return posicao