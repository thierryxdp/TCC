def primo(n):
    '''dado um numero inteiro positivo, verifica se este numero é primo ou nao. int->bool'''
    for i in range(2,n):
        if n%i!=0:
            return True
        else:
            return False