def primo(n):
    divisores = 0
    for numero in range(1,(n**0.5)):
        if n % numero == 0:
            divisores += 1
            
    return divisores < 2