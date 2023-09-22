def primo(n):
    
    
    for divisores in range(1,n//2):
        if n%divisores==0:
            return False
        if n%divisores!=0:
            return True