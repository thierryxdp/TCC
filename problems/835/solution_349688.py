def melhor_volta(m):
    mins = []
    for i in m:
        mins.append(min(i))
    a = min(mins)
    mr = mins.find(a) + 1
    return (mr, a, )