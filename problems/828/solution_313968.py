def primo(n):
    '''função que, dado um número(n),inteiro e positivo, verifica
    se o número é primo ou não.
    int->bool'''
    if n >=2:
        for i in range(2,n):
            if not(n%i):
                return False
        else:
            return True