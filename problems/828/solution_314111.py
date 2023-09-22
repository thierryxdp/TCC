def primo(n):
    divisores = 0
    for numero in range(n):
        if n % numero == 0:
            divisores += 1
            
    return divisores < 2