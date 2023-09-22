def posLetra(string,letra,numero):
    '''retorna a posicao em que a ocorrencia da letra dada como entrada está
    tupla -> int'''
    string.replace(letra,numero,3-1)
    if numero<=str.count(string,letra):
        return str.index(string,letra,numero)
    else:
        return -1