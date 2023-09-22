def fatorial(n):
    '''funcao que recebe um numero e é retornado o seu fatorial
    int->int'''
    if n==0 or n==1:
        return 1
    if n>1:
        i=0
        while (n-1>0):
            i=n*(n-1)
        n-1= n-1-1
        return i