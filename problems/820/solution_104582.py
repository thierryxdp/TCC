def posLetra(string,z,n):
    ''' Retorne em que posição
    da string aquela ocorrencia
    da letra está. str,str,int -> int '''
    i = 0
    c = 0
    while i < len(string):
        if z == string[i]:
            c = c + 1
        if c == i:
            return i
        i = i + 1
        
    return -1