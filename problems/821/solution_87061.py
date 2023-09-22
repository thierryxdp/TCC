def fatorial(x):
    a = 0
    num = 1
    b = list(range(x+1))[1::]
    while a < (len(b)):
        num = num*(b[a])
        a += 1
    return num