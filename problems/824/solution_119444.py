def f(e):
    if e in ('a','e','i','o','u'):
        return e
    return str.upper(e) 
def mapeia(s,f):
    r=[]
    for e in s:
        r.append(f(e))
    return r

def uppCons(s):
    return mapeia(s,f)