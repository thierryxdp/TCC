def qtd_divisores(n):
    ''' Retorna quantos divisores(int) um número n(int) tem. '''
    n_div = 0
    for x in range(1,n+1):
        if n % x == 0:
            n_div += 1
    return n_div
def primo(n):
    ''' Retorna(bool) se o número n(int) é primo.'''
    num = qtd_divisores(n)
    if num > 2:
        return False
    else:
        return True