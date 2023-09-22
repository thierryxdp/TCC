def fatorial (num):
    """ """
    i = 1
    fatorial = num
    while num > 1:
        fatorial *= (num-1)
        i += 1
        num -= 1
    return fatorial