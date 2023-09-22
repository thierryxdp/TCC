def busca(setor:str,matriz:list)->list:
    """ A função recebe uma matriz 3x4, e cada coluna dessa 
    matriz, se refere ao nome, registro,setor e telefone do 
    funcionário. Essa função faz uma busca por setor.Os 
    dados dos funcionários daquele setor, são retornados por
    essa função"""
    for i in range(len(matriz)):
        busca = []
        for j in range(len(matriz[0])):
            if matriz[i][j] == setor:
                list.append(busca,matriz[0])
            else:
                busca
    return busca