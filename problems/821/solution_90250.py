def fatorial(x):
    if x<2:
        return 1
    else:
        return x*fatorial(x-1)