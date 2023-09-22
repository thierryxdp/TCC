def primo(n):
    
    
    x=(n+2)//2
    
    for i in range(2,x):
        
        if n%i==0:
            return False
        
    else:
        return True