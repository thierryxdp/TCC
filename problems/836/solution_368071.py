def busca(setor, matriz):
    """Funcao que recebe um setor como string e uma matriz que em 
    cada linha tem 4 entradas referentes a nome, registro, setor e telefone
    de um funcionario e a partir dessas informacoes consegue fazer a busca
    de todos os funcioinarios daquele setor."""
    
    #Criar uma lista para a matriz de setor filtrado
    matrizFiltrada = []
    
    #Passar pelas linhas
    for i in range (len(matriz)):
        #Passar por todos elementos da lista
        for j in range(i):
            #Se setor for igual, adicionar a lista de matriz filtrado 
            if setor in matriz[i]:
                matrizFiltrada.append(matriz[i])
	
    for i1 in range(len(matrizFiltrada)):
        for j1 in range(i1):
            del(matrizFiltrada[i1][2])
                
    #se a lista for vazia retornar nao encontrou 
    if matrizFiltrada == []:
        return []
    
    # se nao retornar lista
    else:
        return matrizFiltrada