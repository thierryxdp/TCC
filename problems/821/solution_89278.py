def fatorial(n):
    i = 0
    s = 0
    while i<n:
        if n == 0:
            return 0
        else:
            n = n*(n-1)
        	i = i + 1
    return n