def melhor_volta(a):
    c = []
    for i in a:
        for j in i:
            if a[i][j] == min(a[i]):
				list.append(c, a[i][j])
    k = c.index(min(c))
    v = a[k].index(min(c))
    return (k, c, v)