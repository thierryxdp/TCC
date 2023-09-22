def fatorial(num):
    
    i = num
    f = num
    while i != 1:
        f = f * (f-1)
        i = i - 1

    return f