def posLetra(string,letra,numero):
    """Calcula e retorna"""
    i=0
    posicao=-1
    posicoes=0
    while str.count(string,letra)>=numero and i<len(string) and posicoes==numero:
        if string[i] == letra:
            posicao = i
            posicoes=posicoes+ 1
        i=i+1
    return posicao