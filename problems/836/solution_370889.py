def busca(setor: str, matriz: list) -> list:
    """ Função que recebe o nome do setor e uma lista de funcionarios e retorna
    outra lista, com os funcionarios do setor mencionado 
    str, list(list) -> list """
    
    funcionarios_encontrados=[]
    
    
    for i in range(len(matriz)):
        
        if setor == matriz[i][2]:
            
            list.remove(matriz[i], setor)
            list.append(funcionarios_encontrados, matriz[i])
    
    return funcionarios_encontrados