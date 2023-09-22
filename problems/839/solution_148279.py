def carros(p,c=5):
    a=p/c
    if a==int(a):
        return a
    elif a!=int(a) and a>int(a):
        return int(a)+1
    elif a!=int(a) and a<int(a):
        return int(a)
    else:
        return 1