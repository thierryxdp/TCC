def primo(n):
    '''dado um numero inteiro positivo verifica se é primo ou não
    int -> booleano'''
    divisores = []
    for i in range(1,n):
        if n%i ==0 and i!=1 and i!=n:
            return False
        else:
            return True