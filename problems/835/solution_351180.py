def melhor_volta(mat):
    m=[]
    v=[]
    for i in range(len(mat)):
        list.append(m,min(mat[i]))
        list.append(v,list.index(mat[i],m[i]))
    corredor=list.index(m,min(m))
    tempo=min(m)
    volta=v[corredor]
    return ((corredor+1,tempo,volta+1)