def primo(n):
    '''Dado um número inteiro, retorna False se o número
    não for primo e True se for primo.
    int --> bool'''
    proximo = 1
    counter = 1
    while proximo != n:
        if n == 2 or n == 1:
            return True
        elif n%2 == 0 and n!=2:
            return False
        elif n%proximo == 0:
            counter = counter + 1
        proximo = proximo + 2
    if counter > 2:
        return False
    else:
        return True