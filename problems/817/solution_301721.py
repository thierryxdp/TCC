def maiores (l):
    list.append (l)
    list.sort (l)
    return l[((list.index(l)) + 1): ]
def acima_da_media (l):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    if "5" in l:
        a = 5
    if "6" in l:
        b = 6
    if "7" in l:
        c = 7
    if "8" in l:
        d = 8
    if "9" in l:
        e = 9
    if "10" in l:
        f = 10
    return maiores(a+b+c+d+e+f)