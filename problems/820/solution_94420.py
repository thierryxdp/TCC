def posLetra(frase,letra,n):
    ''' '''
    pos = 0
    i = 0
    
    while i < len(frase):
        if frase[i] == letra:
        	pos = pos + 1
        i = i + 1
        if frase[i] != letra:
        	i = i + 1
    return pos