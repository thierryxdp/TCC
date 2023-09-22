def busca(setor,matriz):
    m=matriz
    s=setor
    registro=[]
    for i in range(0,len(m)):
        if s in m[i]:
            del m[i][2]
            registro+=[m[i]]
    return registro