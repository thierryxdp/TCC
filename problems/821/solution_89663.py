def fatorial(x):
    i = x
    while i > 0:
        x *= x-1
    i -= 1
    return x