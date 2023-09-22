def busca(setor,matriz):
    ''' Dada como entrada o nome de um setor da empresa e uma matriz contendo
    os dados dos funcionarios, a funcao retorna uma outras matriz apenas com 
    os que pertencem ao setor escolhido;
    
    str, list -> list ''' 
    
    resultadoBusca = []
    
    for funcionario in matriz: 
        
        if funcionario[2] == setor:
            
            list.append(resultadoBusca,[funcionario[0],funcionario[1],funcionario[3]])
            
    return resultadoBusca