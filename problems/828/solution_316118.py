def primo(n):
    ''' verifica se um numero inteiro positivo é ou não primo,
    int->bool'''
    for num in range(2,n):
        if n%num==0:
            return False
        else:
            return True