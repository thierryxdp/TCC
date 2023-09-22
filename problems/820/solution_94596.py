def posLetra(frase,letra,n):
    ''' '''
    i = 0
    pos = 0
    frase = str.split(frase)
    
    while i < len(frase):
        if frase[i] == letra:
            pos = pos + 1
        	i = i + 1
        return pos