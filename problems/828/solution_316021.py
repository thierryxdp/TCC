def primo(n):
    '''função que recebe um número positivo e inteiro, e 
    verifica se ele éprimo, ou não'''
    if n >=2:
        for i in range(2,n):
            if not (n%i):
                return False
    else:
        return False
    return True