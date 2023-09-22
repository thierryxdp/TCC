def busca(setor,matriz):
    func=[]
    for i in matriz:
            if setor in i:
                func+=[i[0],i[1],i[3]]
    return func