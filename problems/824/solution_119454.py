def uppCons(x):
    r=[]
    for e in ('a','e','i','o','u','á','é','í','ó','ú'):
        return  e   
    return str.upper(e)

def mapeia(s,f):
    r=[]
    for e in s:
        r.append(f(e))
    return r

def upCons(s):
    return str.join('',mapeia(s,f))