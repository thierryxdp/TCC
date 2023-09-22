def fatorial(n):
    '''funcao que dado um numero calcula
    o seu fatorial; int  -> int'''
    i = 1
    fatores = 0
    while i < n:
        fatores = fatores + (n-i)
    return n * fatores