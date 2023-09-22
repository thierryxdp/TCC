def repetidos(x):
    resp = 0
    while a < len(x):
        if x[a] == x[a+1]:
            resp += 1
        a += 1
    return resp