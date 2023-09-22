def busca(tey,tey2):
    t=[]
    for i in range(len(tey2)):
        for c in range(len(tey2[0])):
            if tey in tey2[i][c]:
                tey2.remove(tey)
                t.append(tey2[c])
    return t