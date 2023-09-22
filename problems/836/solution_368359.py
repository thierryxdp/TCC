def busca(x, m):
    y=[]
    for i in range(len(m)):
        if (x in m[i]):
            list.append(y,m[i])
            list.remove(y[i],x)
    return y