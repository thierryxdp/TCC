def busca(setor:str,matriz:list)->list:
    """ A função recebe uma matriz 3x4, e cada coluna dessa 
    matriz, se refere ao nome, registro,setor e telefone do 
    funcionário. Essa função faz uma busca por setor.Os 
    dados dos funcionários daquele setor, são retornados por
    essa função"""
    busca =[]
    for i in range(len(matriz)):
        buscas = []
        for j in range(len(matriz[0])):
            if matriz[i][j] == setor:
                list.append(buscas,matriz[0])
        list.append(busca,buscas)        
    return busca