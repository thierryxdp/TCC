def primo(n):
    
    for i in range(2,int(sqrt(n))):
        if not n%i:
            return False
    return True