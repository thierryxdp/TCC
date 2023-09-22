def primo(n):
    '''Essa função rece um numero inteiro positivo e verifica se é um numero primo ou não
    int -> bool'''
    cont = 0
    for x in range(1, n+1):
        if n % x == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False