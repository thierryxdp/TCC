def filtraMultiplos(a:list,b:int) -> list:
    c = a.pop(b)
    return c
    if c%b == 0:
        return a.pop(c)