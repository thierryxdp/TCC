def primo(n):
    ''' verifica se um numero inteiro positivo é ou não primo,
    int->bool'''
    for numero in range(n-3):
        if (numero+2)%n==0:
            return False
        else:
            return True