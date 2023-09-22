def fatorial(n):
    ''' retorna o fatorial do numero dado, int->int'''
    num=1
    while n>=1 :
        num=num*n
        n=n-1
    return num