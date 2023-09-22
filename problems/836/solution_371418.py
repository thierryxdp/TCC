def busca(setor,matriz):
    funcionarios=[]
    for i in matriz:
        if setor in i:
            funcionarios+=[[i[0],i[1],i[3]]]
    return funcionarios