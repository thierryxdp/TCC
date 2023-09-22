def primo(n):
    '''Entre com um numero para saber se ele primo ou não
    Int -> Bool'''

    x=True
    y=2
    for y in range(n+1):
        if n%y==0:
            x = False
            
    if x and n != 1: 
        return True
    else:
        return False