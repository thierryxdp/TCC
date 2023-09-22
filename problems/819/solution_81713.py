def filtraMultiplos(a:list,b:int) -> list:
    c = a[0:1]
    if c%b == 0:
        return a.pop(c)