def busca(setor:str,matriz:list)->list:
    '''Função que busca na matriz, com informações dos funcionários, quais pertencem ao setor solicitado.'''
    matriz_vazia=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if setor in matriz[i]:
                matriz_vazia.append(matriz[i][2:]+matriz+[1[3:]])
    return matriz_vazia