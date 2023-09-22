def fatorial(n):
    i=0
    fatorial = 0
    if n == 1:
        fatorial =1
    else:
        while 1 < n:
            fatorial = n*i
            i=i+1
    return fatorial