def busca(setor,matriz):
    
    funcionarios=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            
            if matriz[i][j]==setor:
                list.append(funcionarios,matriz[i][0:2]+matriz[i][3:])
                
                
    return funcionarios