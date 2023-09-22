def primo(n):
    '''Dado um número inteiro, retorna False se o número
    não for primo e True se for primo.
    int --> bool'''
    proximo = 1
    counter = 0
    while proximo != n:
        if n%2 == 0:
            return False
        if n%proximo == 0:
            counter = counter + 1
        proximo = proximo + 1
    if counter > 2:
        return False
    else:
        return True