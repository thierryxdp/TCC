def busca(setor, matriz):
    """recebe uma matriz contendo os dados de funcionarios de uma empresa e 
    um setor dessa empresa, e retorna uma lista contendo os dados de todos os
    funcionarios daquele setor
    string, list -> list"""
    
    funcionarios = []
    
    linha = len(matriz)
    
    for i in range(linha):
        if setor in matriz[i][2]:
            list.append(funcionarios, matriz[i][0:2] + matriz[i][3:])
            
    return funcionarios