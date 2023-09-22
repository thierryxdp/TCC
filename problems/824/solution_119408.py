def f(x):
    if x in ('a','A','á','e','E','é','i','I','o','O','ó','u','U'):
        return x
    else:
        return str.upper(x)
def map(it,p):
    r=[]
    for i in it:
        r.append(p(i))
    return r
def uppCons(fr):
    return ''.join(map(fr,f))