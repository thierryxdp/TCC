def primo(n):
    '''Função que descobre se um número é primo ou não.
    int --> bool'''
    divisores = []
    for numero in range(2,n):
        if n%numero == 0:
            divisores = divisores + [numero]
    if divisores == []:
        return True
    else:
        return False