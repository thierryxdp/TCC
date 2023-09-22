def repetidos(l):
    i = 0
    ie = 0
    while i <= len(l):
        if l[i+1] != l[i] and i != 0:
            i = i + 1
        else:
            i = i + 1
            ie = ie
    return ie