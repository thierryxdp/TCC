def fatorial(n):
    i = 0
    multiplicatorio = 1
    while i<n:
        multiplicatorio = multiplicatorio*(n-i)
    i = i + 1
    return multiplicatorio