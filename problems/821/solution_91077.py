def fatorial(n):
    ''' Código que calcula fatorial de n 
    :n --> int:
    :f --> int:
    '''
    y=n
    f=1
   
    while y>1:
        f=y*(y-1)*f
        y=y-2
        
    i=+1
    return f