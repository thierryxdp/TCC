def posLetra(string,car,n):
    '''Funcao que retorna em que posicao a string esta'''
    c=0
    i=0
    while i<len(string):
        if string[i] == car:
            c=c+1
        if c==n:
            return i
        i=i+1
    return -1