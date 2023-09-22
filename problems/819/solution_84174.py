def filtraMultiplos(x,y):
    r = []
    for item in x:
        if item%y == 0 :
            r = r + [item, ]
            return r