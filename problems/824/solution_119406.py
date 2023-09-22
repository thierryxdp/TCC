def f(x):
    if x in ('a','A','e','E','i','I','o','O','u','U'):
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