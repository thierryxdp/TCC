def primo(n):
    """ Dado um número inteiro positivo, ver se este número é primo
    int-> bool"""
    c = 0
    for fator in range(1, n+1):
        if n % fator == 0:
            c +=1
        if c ==2:
            return True
        else:
            return False