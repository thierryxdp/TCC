def busca(y,x):
    a=[]
    for i in range(len(x)):
        if y in x[i]:
            a.append(x[i])
    for k in range(len(a)):
        if y in a[k]:
            a[k].remove(y)
        
    return a