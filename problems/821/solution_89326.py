def fatorial(num):
    x = 1
    y = 0
    while 0 < x < num and 0 < num :
        if num > 0:
            y = y + (num * x)
        num = num -1
        x = x +1

    return y