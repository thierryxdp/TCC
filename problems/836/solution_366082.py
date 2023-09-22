def busca(setor,matriz):
    
    funcionarios=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            
            if matriz[i][j]==setor:
                list.append(funcionarios,matriz[i][0])
    return funcionarios