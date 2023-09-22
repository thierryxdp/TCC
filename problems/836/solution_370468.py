def busca(setor, matriz):
    '''recebe uma matriz e faz uma busca por setor retornando os dados de todos
    os funcionarios daquele setor
    matriz -> matriz'''
    
    resultMatriz = []
    
    for funcionario in matriz:
        if(funcionario[2].upper() == setor.upper()):
            resultMatriz.append(funcionario)
   	
    
    return resultMatriz