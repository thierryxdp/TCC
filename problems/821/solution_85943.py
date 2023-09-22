def fatorial(n):
    '''funcao que recebe um numero e é retornado o seu fatorial
    int->int'''
    if n==0 or n==1:
        return 1
    if n>1:
        fatorial=1
        while n>0:
            fatorial = fatorial*n
            n=n-1
        return fatorial