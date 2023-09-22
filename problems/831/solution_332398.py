def lingua_p(port):
    '''
    '''
    x=str.lower(port)
    i=0
    portugues=''
    while i<len(x):
        if x[i] not in "aeiouáéú":
            portugues=portugues+x[i]
        
        else:
            portugues=portugues+x[i]+"p"+x[i]
        i=i+1
    return portugues