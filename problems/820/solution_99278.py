#
#
#
#
def posLetra(string,letra,numero):
    i=0
    j=1
    while i < len(string):
        if j <= numero:
            if string[i] == letra:
                posicao=i
                j=j+1
    i=i+1    
        
    return posicao