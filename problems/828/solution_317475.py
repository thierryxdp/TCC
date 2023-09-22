def primo(n):
    '''
    Dado um numero inteiro positivo, a função verifica 
    se este numero é primo ou nao e retorna True or False
    int --> bool
    '''
    primo = 0
    for x in range(1, n+1):
        if n % x == 0:
            primo += 1
    if primo == 2:
        return True
    else:
        return False