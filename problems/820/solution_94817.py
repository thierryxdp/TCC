def posLetra(string,l,o):
    ''' l = letra , o = ocorrencia.'''
    i=0
    c=0
    while i < len(string):
        if string[i]==l:
            c=c+1
        if c==o:
            return i
        i<=1
    return i