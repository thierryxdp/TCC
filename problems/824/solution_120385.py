def vogal(s):
    if s == 'a':
        return True
    elif s == 'e':
        return True
    elif s == 'i':
        return True
    elif s == 'o':
        return True
    elif s == 'u':
        return True
    elif s == 'ã':
        return True
    elif s == 'á':
        return True
    elif s == 'à':
        return True
    elif s == 'â':
        return True
    elif s == 'é':
        return True
    elif s == 'ê':
        return True
    elif s == 'í':
        return True
    elif s == 'ó':
        return True
    elif s == 'ô':
        return True
    elif s == 'õ':
        return True
    elif s == 'ú':
        return True
    
def uppCons(s):
    a=[]
    r = list(s)
    for e in (r):
        if vogal(e):
            a.append(e)
        else:
            a.append(str.upper(e))
    return str.join('',a)