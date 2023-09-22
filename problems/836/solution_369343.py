def busca(setor:str,matriz:list)->list:
    """ A função recebe uma matriz 3x4, e cada coluna dessa 
    matriz, se refere ao nome, registro,setor e telefone do 
    funcionário. Essa função faz uma busca por setor.Os 
    dados dos funcionários daquele setor, são retornados por
    essa função"""
    busca =[]
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            list.append(busca,(list.remove(matriz[i],setor))
        else:
            busca        
    return busca