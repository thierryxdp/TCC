def repeditos (l):
    v = 0
    for e in l:
        if l[e] == l[e-1]:
            return v+=1