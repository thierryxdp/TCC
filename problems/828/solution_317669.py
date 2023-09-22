def primo(a):
    '''
    
    '''
    x=0
    for count in range(2,a):
        if (a%count==0):
            x+=1
        if (x==0):
            return True 
        else: 
            return False