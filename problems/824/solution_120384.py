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
def uppCons(s):
    a=[]
    r = list(s)
    for e in (r):
        if vogal(e):
            a.append(e)
        else:
            a.append(str.upper(e))
    return str.join('',a)