def repetidos(l):
    i = 0
    ie = 0
    leng = len(l)
    while i < len(l) - 1:
        if l[i] == l[i+1]:
            ie = ie + 1
            i = i + 1
        elif i == len(l) - 1:
            ie = ie
        else:
            i = i + 1
    return ie