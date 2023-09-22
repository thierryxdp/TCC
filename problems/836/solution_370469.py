def busca(setor, matriz):
    '''recebe uma matriz e faz uma busca por setor retornando os dados de todos
    os funcionarios daquele setor
    matriz -> matriz'''
    
    resultMatriz = []
    
    for funcionario in matriz:
        if(funcionario[2].upper() == setor.upper()):
            newData = [funcionario[0], funcionario[1], funcionario[3]]
            resultMatriz.append(newData)
   	
    
    return resultMatriz