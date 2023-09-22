def busca(x, m):
    y=[]
    for i in range(len(m)):
        if (x in m[i]):
            list.append(y,m[i])
            for j in range(len(y)):
                if ( x in y[j]):
                list.remove(y[j],x)
    return y