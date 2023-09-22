#
#
#
#
def posLetra(string,letra,numero):
    i=0
    j=1
    posicao = int
    while i < len(string) and j <= numero:
        if string[i]==letra:
            posicao = i +1        
    i=i+1       
    return posicao