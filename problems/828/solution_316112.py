def primo(n):
    ''' verifica se um numero inteiro positivo é ou não primo,
    int->bool'''
    for numero in range(n):
        if n%numero==0:
            return False
        else:
            return True