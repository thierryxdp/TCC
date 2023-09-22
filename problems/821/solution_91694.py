def fatorial(n):
    l = list(range(n, 0, -1))
    ls = list(range((n-1), 0, -1))
    for i in l:
        for j in ls:
            i = i*j
            return i