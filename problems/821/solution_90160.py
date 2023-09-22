def fatorial(n):
    N = n
    a = 1
    while a < N:
        n = n*(N-a)
        a = a + 1
    return n