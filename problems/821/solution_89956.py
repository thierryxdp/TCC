def fatorial(n):
    proximo=1
    fatorial=1
    while proximo <= n:
        fatorial=proximo*fatorial
        proximo = proximo + 1
    return fatorial