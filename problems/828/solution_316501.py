def primo(n):
    '''dado um numero ele verifica se ele é um numero primo'''
    cont_divisores = 0

    for divisor in range(1,n+1):
        if n % divisor == 0:
            cont_divisores += 1 

    if cont_divisores == 2:
        return True
    else:
        return False