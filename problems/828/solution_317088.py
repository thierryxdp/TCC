def primo(x):
    '''
    '''
    
    for i in range(2,x):
        if x % i ==0:
            x+=1
            
    if x>0:
        
        return True
    
    else:
        
        return False