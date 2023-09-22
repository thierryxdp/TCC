def busca(setor, matriz):
    '''a funcao retorna os funcionarios do setor de entrada
    str,list->list'''
    funcionarios=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if setor in matriz[i][j]:
                del matriz[i][2]
                funcionarios= funcionarios + [matriz[i]]
                
                
                
    return remove