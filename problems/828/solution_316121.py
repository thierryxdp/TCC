def primo(n):
    ''' verifica se um numero inteiro positivo é ou não primo,
    int->bool'''
    for num in range(2,n):
        if num%n==0:
            return False
        else:
            return True