def melhor_volta(matriz):
    m=[]
    v=[]
    for i in range(len(matriz)):
        list.append(m,min(matriz[i]))
        list.append(v,list.index(matriz[i],m[i]))
    corredor=list.index(m,min(m))
    tempo=min(m)
    volta=list.index(v,corredor)
    return ((corredor+1,tempo,volta+1))