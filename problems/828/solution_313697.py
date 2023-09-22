def primo(n):
    
    
    for divisores in range(0,n//2+1):
        if n%divisores==0:
            return False
        if n%divisores!=0:
            return True