def busca(setor: str, matriz: list) -> list:
    """"""
    funcionarios_encontrados=[]
    matriz_copi= matriz[:]
    
    for i in range(len(matriz)):
        
        if setor == matriz[i][2]:
            
            list.remove(matriz_copi[i], setor)
            list.append(funcionarios_encontrados, matriz_copi[i])
            return funcionarios_encontrados
        
    return funcionarios_encontrados