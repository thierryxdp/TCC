def posLetra(string,letra,numero):
    posicao= str.find(string,letra)
    while numero>1:
        if str.count(string,letra)>numero:
            posicao= str.find(string,letra,posicao+1)
        x= x - 1
        else:
            posicao= -1
    return posicao