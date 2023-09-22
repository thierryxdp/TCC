def busca(setor,matriz):
    funcionarios=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            funcionarios+=[matriz[i][::3]]
    return funcionarios