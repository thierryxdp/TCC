def busca(st,m):
    func=[]
    for i in range(len(m)):
        if st in m[i]:
            matriz[i].remove(st)
            y = y + matriz[i]
    return y