def primo(n):
    '''dado um numero inteiro positivo verifica se é primo ou não
    int -> booleano'''
    divisores = []
    for i in range(0,n):
        if n%i ==0 and i!=1 or i!=n:
            return False
        else:
            return True