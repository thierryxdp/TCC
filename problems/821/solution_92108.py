#calcula o fatorial de um numero n
#int-->int
def fatorial(n):
    x=1
    for f in range(1, n+1):
        x*=f
    return x