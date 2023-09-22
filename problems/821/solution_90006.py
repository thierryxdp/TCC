def fatorial(n):
    "Dado um número, cálcula seu fatorial; int -> list"
    if n < 2:
        return 1
    else:
        return n * fatorial(n-1)