def f(e):
    if e in ('a','e','i','o','u','ã','õ','á','é','í','ó','ú'):
        return e
    return str.upper(e) 
def mapeia(s,f):
    r=[]
    for e in s:
        r.append(f(e))
    return r

def uppCons(s):
    return str.join('',mapeia(s,f))