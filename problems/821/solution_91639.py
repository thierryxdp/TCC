def fatorial(n):
    '''função em que dada um número, calcule o fatorial deste número'''
    i=1
    j=1
    while i<=n:
        j*=i
        i+=1
        return j