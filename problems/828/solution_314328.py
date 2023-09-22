def primo(numero):
    
    
    for num in range(2,numero//2+1):
        if numero % num == 0:
            return False
        
    else:
        return True