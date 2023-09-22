def primo(n):
    '''função que dado um número inteiro positivo retorna se ele é primo ou não:int->booleano'''
    n_divisores = 0
    for divisor in range(1,n+1):
        if n % divisor == 0:
            n_dividores =+ 1
    if n_divisores == 2:
        return True
    else:
        return False