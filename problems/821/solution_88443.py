def fatorial(num):
    """..."""
    fat = 0
    i = 0
    while i>1:
        if num < 0:
            fat = 0
        elif num == 0 or num == 1:
            fat = 1
        else:
            fat = fat*num
            n -= 1
    return fat