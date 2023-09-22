def primo(n):
    numero_divisores = 0
    for i in range(1, n):
        if(n % i == 0):
            numero_divisores = numero_divisores + 1
    
    if(numero_divisores > 2):
        return False
    else:
        return True