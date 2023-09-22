def primo(n):
    '''dado um numero inteiro positivo, verifica se este ńumero ́e primo
ou nao. Retorna um valor booleano.'''
    mult=0
    for count in range(2,n):
        if (n % count == 0):
            return False
    return True