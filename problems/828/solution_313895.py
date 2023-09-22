def primo(n):
    '''Função que dado um número como entrada retorne se este
    número é primo ou não. int --> bool.'''
    x=0
    for n in range(2,n):
        if n%x==0:
            return False 
    return True