def divisivel(x):
    r = 0
    for i in range(x):
        if x%(i+1) == 0:
            r = r + 1