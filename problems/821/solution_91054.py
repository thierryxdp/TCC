def fatorial(n):
    i=1
    fatorial = 0
    while i <= n:
        fatorial=n*i
        fatorial = fatorial*i
        i=i+1
    return fatorial

fatorial(1)