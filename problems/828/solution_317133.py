def primo(n):
    
    for i in range(2,n):
        
        if n%i==0:
            return False
        if i**2==n:
            return False
        else:
            return True