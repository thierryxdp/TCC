def repeditos (l):
    v = 0
    for e in l:
        if l[(list.index(l,e))] == l[(list.index(l,e-1))]:
            return v+=1