def primo(n):
    divisores = 0
    for numero in range(1,n):
        if n % numero == 0:
            divisores += 1
            
    return divisores < 2