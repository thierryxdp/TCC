def melhor_volta(m):
    t =()
    l = []
    for i in range(len(m)):
        for k in range(len(m[0])):
            l.append(m[i][k])
    x = min(l)
    return x