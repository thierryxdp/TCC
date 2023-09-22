def primo(n):
    
    
    for divisores in range(1,n//2+1):
       
        if n%divisores!=0:
            return True
        else:
            return False