def filtraMultiplos(a:list,b:int) -> list:
    c = str(a)
    e = c.replace('[','').replace(']','')
    f = a.partion(',')
    d = int(f)
    return e