def busca(setor,matriz):
    r=[]
    for i in matriz:
        if i[2]==setor:
            a=i[0]+i[1]+i[3]
            r+=a
            
    return r