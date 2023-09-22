def busca(setor, matriz):
    '''a funcao retorna os funcionarios do setor de entrada
    str,list->list'''
    funcionarios=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if setor in matriz[i][j]:
                funcionarios= funcionarios + [matriz[i]]
                
    for i in range(len(funcionarios)):
        for j in range(len(funcionarios[0])):
            remove=remove+del funcionarios[i][2]
              
                
                   
    return remove