def primo(n):
    '''dado um numero inteiro positivo, verifica se este numero é primo ou nao. int->bool'''
    for i in list(range(2,n)):
        if n%i==0:
            return False
        else:
            return True