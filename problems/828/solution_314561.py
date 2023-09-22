def primo(x):
    'retorna se x é primo ou não'
    divisores = 0
    for numeros in range(1,x+1):
        if x%numeros == 0:
            divisores = divisores + 1
    if divisores == 2:
        return divisores == 2
    
    elif divisores > 2:
        return divisores == 2