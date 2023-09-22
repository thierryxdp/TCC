def primo(n):
    '''função que retorna True se o numero n for primo e False caso contrário;
    int --> bool'''
    num_divisores = 0
    for divisor in range(1,n+1):
        if n % divisor == 0:
            num_divisores = num_divisores + 1
    if num_divisores == 2:
        return True
    else:
        return False