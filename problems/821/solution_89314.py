def fatorial(num):
    x = num
    y = 0
    while x >= 1:
        if x>0:
            y = x*(x-1)
        x = x -1
        
    return y