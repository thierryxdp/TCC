def fatorial(n):
    mult = 1
   # for m in range(1, n):
    #    m = mult * m
     #   fatn = n * m
   # return fatn
    prox = 1
    while prox < n:
        m = (prox - 1) * prox
        prox = prox + 1
    fatn = n * m
    return fatn