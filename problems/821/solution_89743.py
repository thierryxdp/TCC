def fatorial(num):
    """fatorial do número """
    n = num - 1
    while n > 0:
        num = num * n
        n += -1
    return num