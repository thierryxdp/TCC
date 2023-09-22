def primo(n):
    
    for i in range(1,n):
        if not n%i:
            return False
    return True