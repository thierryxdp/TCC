def fatorial(n):
    """Dado um número "n" calcula seu fatorial
    int -> int"""
    fat = 1
    while n>0:
        fat = fat*n
        n = n-1
    return fat