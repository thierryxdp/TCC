def fatorial(n):
    '''funcao que calcula o fatorial de um numero
    entrada:int
    saida:int'''
    prod=1
    while n>0:
        prod*=n
        n=n-1
    return prod