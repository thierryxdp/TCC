def fatorial(n):
    proximo=n
    fatorial=0
    while proximo >= 1:
        fatorial=proximo*(n-1)
    proximo = proximo - 1
    return fatorial