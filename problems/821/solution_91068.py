def fatorial(n):
    i=0
    fatorial = 0
    while i < n:
        if n == 1:
            fatorial =1
        else:
            fatorial = n*i
            i=i+1
    return fatorial