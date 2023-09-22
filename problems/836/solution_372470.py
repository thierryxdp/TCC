def busca(setor,matriz):
    funcionario=[]
    for pessoa in range(len(matriz)):
        if setor in matriz[pessoa]:
            funcionario.append(matriz[pessoa])
    return funcionario