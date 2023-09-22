def melhor_volta(a):
    c = []
    for i in a:
        for j in i:
            if j == min(a[i]):
				list.append(c, j)
    k = c.index(min(c))
    v = a[k].index(min(c))
    return (k, c, v)