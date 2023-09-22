def primo(n):
    '''Funcao que dado um numero inteiro positivo, verifica
    se este e primo ou nao
    int -> bool'''
    mult = 0
    for elemento in range(2,n):
        if n%elemento == 0:
            mult += 1
    if mult == 0:
        return True
    else:
        return False