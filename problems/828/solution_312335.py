def primo(n):
    '''Dado um numero n, retorna True se o numero for primo e False se nao for.
    int -> bool'''
    mult = 0

    for i in range(1, n):
        if (n % i == 0):
            mult += 1
            if mult > 0:
                return False
    return True