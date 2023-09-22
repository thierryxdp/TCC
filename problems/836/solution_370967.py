def busca(setor,matriz):
    '''dada uma matriz e um setor, retorna todos os 
    funcionários daquele setor;list,str -> list'''
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    listafinal = []
    
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == setor:
                list.remove(matriz,setor)
                listafinal.append(matriz[i])
  
    return listafinal