def primo(n):
    '''Entre com um numero para saber se ele primo ou não
    Int -> Bool'''

    x=False
    y=False
    N=0
    
    if n%n==0:
        y=True
        
    for y in range(n+1):
        y=y+1
        if y<=n:
            if n%y==0:
            	x = True
                N=N+1
                
   	if y==True and x == True and N==1:
        return True
    
    else:
        return False