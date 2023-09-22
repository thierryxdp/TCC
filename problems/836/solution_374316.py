ef busca(area, matriz):
    """
    função que recebe uma matriz e faz uma busca por setor, retornandoo os dados de todos os
    funcionários daquele setor
    
    str,list--->list
    """
    
    resultado = []
    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz[linha])):
            if area.lower() == matriz[linha][coluna].lower():
                dados = matriz[linha].copy()
                dados.pop(dados.index(dados[coluna]))
                resultado.append(dados)

    return resultado