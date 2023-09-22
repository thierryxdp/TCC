def posLetra(string,letra,numero):
    """ """
    indice = 0
    while indice < len(string):
        if string.count(letra) < numero:
            return -1
        else:
            primeira = string.index(letra)
            num = numero+1
            posicao = string.index(letra,num+1)
            return posicao