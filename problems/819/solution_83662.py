def filtraMultiplos (x,n):
    
    '''
    '''
    listaM=[]
    y=0
    while y<len(x):
        if x[y]%n==0:
            listaM= listaM+[x[y]]
        y=y+1
    return listaM