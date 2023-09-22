def fatorial(n):
    i = 1
    #não pode ser 0 pq vai multiplicar
    s = 1
    while i < n:
        s = s*i
        i = i + 1
    s = s*n
    return s