def repetidos (l):
    r = 0
    i = 0
    while i < len (l):
        if l[i] == l[i-l]:
            r = r+1
            i = i+1
        else:
            i = i+1
    return r