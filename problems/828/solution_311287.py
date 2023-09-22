def primo(n):
    '''dado um numero inteiro positivo verifica se é primo ou não
    int -> booleano'''
    divisores = []
    for i in range(1,n+1):
        if n%i == 0:
            divisores = divisores + [i,]
    if len(divisores) == 2:
        return True
    else:
        return False