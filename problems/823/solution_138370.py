def faltante(x):
    '''
   	list->int
    '''
    if 1 not in x:
        return 1
    y=0
    z=0
    while z<(len(x)-1):
        if x[z]!=x[z+1]-1:
            y=y+(z+2)
        z=z+1
    if y==0:
               return x[-1]+1
            
    return y