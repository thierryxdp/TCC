def primo(n):
    '''dado um numero n, retorna se ele é primo ou nao
    int -> bool'''
    divisores = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisores += 1
    if divisores <= 2:
        return True
    else:
        return False