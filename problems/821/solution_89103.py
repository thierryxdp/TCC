def fatorial(n):
    proximo=n
    fatorial=0
    while proximo == 0:
        fatorial=proximo*n
    proximo = proximo - 1
    return fatorial