def repetidos(l):
    n = 0
    for i in l:
        if l[i] == l[i-1]:
            n +=1
    return n