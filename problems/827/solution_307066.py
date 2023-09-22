def qtd_divisores(n):
    for i in xrange(1,n/2+1):
        if n%i == 0: yield i
    return n