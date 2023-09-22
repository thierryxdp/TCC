def busca(setor,matriz):
    '''Funcao que recebe uma matriz com dados de funcionarios
    e uma elemento da matriz(setor) e
    retorna os dados de todos os funcionarios daquele setor
    str, list -> list
    '''
    funcionario = [] 
    
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.remove(matriz[i],setor)
            funcionario.append(matriz[i])
            
            
            
    return funcionario