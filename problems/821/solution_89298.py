def fatorial(num):
    x = num
    y = 0
    while x > 0:
        if num > 0:
            y = y + num * x
        x = x -1
        
    return y