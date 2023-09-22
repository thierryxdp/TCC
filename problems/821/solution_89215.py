def fatorial(n):
    i=1
    b=n-1
    fat=n
    while i<=n:
        fat= fat*b
        b=b-1
        i=i+1
    return fat