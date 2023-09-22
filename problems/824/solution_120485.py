def uppCons(d):
    r=[]
    f=['a','e','i','o','u']
    for e in d:
        if e not in f:
            g=e.upper()
            list.append(r,(g))
        else:
            list.append(r,(e))
    return "".join(r)