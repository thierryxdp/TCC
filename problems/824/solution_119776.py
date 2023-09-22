def mapeia(l, f):
    r = []
    for x in l:
        r.append(f(x))
    return r    

def upp(x): 
    if x not in ('a', 'e', 'i', 'o', 'u', 'í', 'á', 'ó', 'ã', 'ú'):
        return x.upper()
    return x

def uppCons(s):
    l = mapeia(s, upp)
    return "".join(l)