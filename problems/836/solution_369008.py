def busca(setor,matriz):
    funcionarios=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            del matriz[i][2]
            funcionarios+=[matriz[i]]
    return funcionarios