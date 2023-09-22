#
#
#
#
def posLetra(string,letra,numero):
    i=0
    posicao=0
    while i<len(string):
        p=str.find(string,letra)
        posicao=posicao+p
        i=i+1
    return posicao