def primo(n):
    '''Dado um número inteiro positivo, verifica se ele
    é primo ou não.
    int -> bool'''
    divisores = []
    for i in range(1,n+1):
        if n%i == 0:
            divisores += [i]
    return divisores == [1,n]