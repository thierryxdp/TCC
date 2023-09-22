def fatorial(n):
    " Fatorial de um numero dado."
    if n ==0:
        return 1
    else:
        return n*fatorial(n-1)