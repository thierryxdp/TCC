def fatorial(n):
    proximo = 1
    fatorial=n
    while proximo<n:
        fatorial = fatorial*(n-proximo)
        proximo = proximo + 1
    return fatorial