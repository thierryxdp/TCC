def primo(n):
    '''primo recebe um numero inteiro positivo n e devolve se este numero é primo ou nao.
    Assume n valores inteiro positivos.
    int-->bool.'''
    if n==2:
        return 0==0
    elif n%2==0:
        return 0==1
    else:
        valores=range(3,n,2)
        divisores=0
        for numero in valores:
            if n%numero==0:
                divisores=divisores+1
        return 0==divisores