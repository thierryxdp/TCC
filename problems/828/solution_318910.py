def primo(x):
    """funcao que dado um inteiro positivo, verifica se e primo ou nao e retorna um valor bool;
    int -> bool"""
    primos = 0
    for i in range(1, x+1):
        if x % i == 0:
            primos += 1
            
    if primos == 2:
        return True
    
    else:
        return False