def primo(n):
    '''Função que dado um número como entrada retorne se este
    número é primo ou não. int --> bool.'''
    for n in range(n,1):
        if n%2 == 0:
            return False 
        else:
            return True
    return primo