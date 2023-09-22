def repetidos(x):
    repetido = 0
    r = 0
    for i in x:
        if i == x[r-1]:
            repetido = repetido + 1
            r = r + 1
        elif i == x[r-1]:
            r = r + 1
        else:
            r = r + 1
    return repetido