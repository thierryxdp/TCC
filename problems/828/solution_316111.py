def primo(n):
    ''' verifica se um numero inteiro positivo é ou não primo,
    int->bool'''
    for numero in range(n):
        if n%(numero+2)==0:
            return True
        else:
            return False