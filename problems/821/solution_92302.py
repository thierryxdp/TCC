def fatorial(n):
    fat=n
    proximo=n-1
    while n-proximo<n:
        fat=fat*(proximo)
        proximo=proximo-1
    return fat