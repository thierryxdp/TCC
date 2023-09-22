def busca(setor,matriz):
    funcionarios=[]
    for i in matriz:
        if setor in i:
            funcionarios+=list.remove(i,setor)
    return funcionarios