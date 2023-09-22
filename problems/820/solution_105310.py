def posLetra(string,letra,numero):
    """Calcula e retorna"""
    i=0
    posicao=-1
    while str.count(string,letra)=numero and i<len(string):
        if string[i] == letra:
            posicao = i
        i=i+1
    return posicao