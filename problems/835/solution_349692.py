def melhor_volta(m):
    mins = []
    for i in m:
        mins.append(min(i))
    a = min(mins)
    mr = mins.index(a) + 1
    v = 1
    for i in m:
        for j in i:
            if j == a:
                v = v + i.index(j)
    return (mr, a, v)