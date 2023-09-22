def posLetra(x,y,z):
    '''Retorna em que posição da frase, a letra está dada a ocorrência.
    str, str, int -> int'''
    str.replace(x, y, '|', z)
    return str.find(x,'|')