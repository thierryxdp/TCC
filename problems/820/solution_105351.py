def posLetra(string,letra,numero):
    """Calcula e retorna"""
    i=0
    posicao=-1
    acumulador=[]
    while str.count(string,letra)>=numero and i<len(string) and len(acumulador)<=numero:
        if string[i] == letra:
            posicao = i
            posicoes=posicoes+ 1
            acumulador=acumulador + [string[i]]
        i=i+1
    return posicao