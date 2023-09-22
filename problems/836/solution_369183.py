def busca(y,x):
    a=[]
    for i in range(len(x)):
        if y in x[i]:
            a.append(x[i])
            a[i].remove(y)
    return a