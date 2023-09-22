def fatorial(num):
    """..."""
    if num < 0:
        return 0
    elif num == 0 or num == 1:
        return 1
    else:
        fatorial = 1
        while(num > 1):
            fatorial = fatorial* num
            num -= 1
        return fatorial