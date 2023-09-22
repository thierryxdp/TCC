def primo(n):
    
    for i in range(n + 1)[2:]:
        if n / i == int(n / i):
            return False
    
    return True