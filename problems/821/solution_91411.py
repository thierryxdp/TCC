def fatorial(n):
    if n >= 0:
        fatorial = 1
        while (n):
            fatorial = fatorial * n
            n = n - 1
    return fatorial