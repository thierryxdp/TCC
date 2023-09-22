def primo(n):
    '''dado um numero inteiro positivo, verifica se este numero é primo ou nao. int->bool'''
    for i in range(n):
        if n%i==0:
            return False
        else:
            return True