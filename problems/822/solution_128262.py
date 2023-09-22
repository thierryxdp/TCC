def repetidos(x):
    D = 0
    r = 0
    for i in x:
        if i == x[r-1]:
            D = D + 1
            r = r + 1
        elif i == x[r-1]:
            r = r + 1
        else:
            r = r + 1
return