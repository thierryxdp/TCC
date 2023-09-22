def uppCons(s):
    a=[]
    r = list(s)
    for e in (r):
    if vogal(e):
    a.append(e)
    else:
    a.append(str.upper(e))
    return str.join('',a)