def busca(area, matriz):
    """
    função que busca um usuário baseado na sua área dentro da empresa.
    :param area: str 
    :param matriz: list 
    :return: list 
    """
    
    busca = []
    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz[linha])):
            if area.lower() == matriz[linha][coluna].lower():
                dados = matriz[linha].copy()
                dados.pop(dados.index(dados[coluna]))
                busca.append(dados)

    return busca