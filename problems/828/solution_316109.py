def primo(n):
    ''' verifica se um numero inteiro positivo é ou não primo,
    int->bool'''
    for numero in range(n):
        if n%(numero+1)==0:
            return true
        else:
            return false