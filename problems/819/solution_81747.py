def filtraMultiplos(a:list,b:int) -> list:
    c = str(a)
    e = c.replace('[','').replace(']','')
    f = e.partition(',')
    d = int(f)
    return e