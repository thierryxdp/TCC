def filtraMultiplos(a:list,b:int) -> list:
    c = a[0:1]
    return c%b
    if c%b == 0:
        return a.pop(c)