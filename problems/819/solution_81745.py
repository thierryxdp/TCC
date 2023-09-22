def filtraMultiplos(a:list,b:int) -> list:
    c = str(a)
    e = c.replace('[','').replace(']','')
    f = e.partion(',')
    d = int(f)
    return e