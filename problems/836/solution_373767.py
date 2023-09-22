def busca(setor,matriz):
    d=[]
    for i in matriz:
        #print(i)
        for j in i:
            #print(j)
            if j==setor:
                d.append(i)
    return d[0:]