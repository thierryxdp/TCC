def primo(n):
    '''Entre com um numero para saber se ele primo ou não
    Int -> Bool'''

    x=False
    z=False
    N=0
    
    if n%n==0:
        z=True
        
    for y in range(n+1):
        y=y+1
        if y<n:
            if n%y==0:
            	x = True
                N=N+1
                
    if z==True and x == True and N==1:
        return True
    
    else:
        return False