def fatorial(num):
    n=num
    f=num-1
    resultado=0
    while f>0:
        resultado+=n*f
        f+=-1
    return resultado