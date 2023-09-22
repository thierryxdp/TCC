def filtraMultiplos(x,y):
    r = []
    for item in x:
        if item/y == int(1):
            r = r + [item, ]
            return r