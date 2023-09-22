def busca(s,m):
    l=[]
    for i in range(len(m)):
        if m[i][2]==s:
            del(m[i][2])
            list.append(l,m[i])
    return l