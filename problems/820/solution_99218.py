def posLetra(texto,letra,n):
    '''
    '''
    i=n
    pos=0
    while i>0:
        pos=str.find(texto,letra,pos+1)
        i=i-1
        if pos==-1:
            return -1
    return pos