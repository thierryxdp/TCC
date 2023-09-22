def fatorial(n):
    i = 0
    multiplicatorio = 1
    while i<n-1:
        multiplicatorio = multiplicatorio*(n-i)
    i = i + 1
    return multiplicatorio