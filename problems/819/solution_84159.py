def filtraMultiplos(x,y):
    r = ()
    for item in x:
        if item/y == 3:
            r = r + (item, )
            return r