def primo(n):
    '''Entre com um numero para saber se ele primo ou não
    Int -> Bool'''

    x=False
    
    for y in range(n+1):
        y=y+1
        if y<=n:
            if n%y==0:
            	x = True
    
    return x