def posLetra(string,z,n):
    ''' Retorne em que posição
    da string aquela ocorrencia
    da letra está. str,str,int -> int '''
    i = 0
    c = 0
    while i < len(string):
        if string[i] == z:
            c = c + 1
      	i = i + 1
        if c == i:
            return i
    return -1