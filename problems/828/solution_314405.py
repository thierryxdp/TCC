def primo(n):
    divisores = 0
    for num in range (1, int((n**0.5) + 1)):
        if n % num == 0:
            divisores += 1
    
    return divisores < 2