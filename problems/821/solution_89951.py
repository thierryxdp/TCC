def fatorial(n):
    proximo=n
    fatorial=0
    while proximo == 1:
        fatorial=proximo*n
    proximo = proximo - 1
    return fatorial