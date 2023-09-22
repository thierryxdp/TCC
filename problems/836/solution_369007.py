def busca(setor,matriz):
    funcionarios=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            s=matriz[i].remove(setor)
            funcionarios+=[s]
    return funcionarios