def repetidos(l, n):
    i = 0
    ie = 0
    while i < len(l):
        if l[i+1] == l[i]:
            i = i + 1
            ie = ie + 1
        else:
            i =  i + 1
            ie = ie
    return ie