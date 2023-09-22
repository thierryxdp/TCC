def posLetra(string,letra,numero):
    '''retorna a posicao em que a ocorrencia da letra dada como entrada está
    tupla -> int'''
    
    if numero<=str.count(string,letra):
        string.replace(letra,numero,3-1)
        return str.index(string,letra,numero)
    else:
        return -1