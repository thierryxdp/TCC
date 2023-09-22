def primo(x):
    '''
    '''
    final=0
    
    for i in range(1,x+1):
        if x % i==0:
            final+=1
            
    if final==2:
        return True
    
    else:
        return False