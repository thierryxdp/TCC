def busca(area, matriz):
    '''Busca um usuário baseado na sua área dentro da empresa.
    :param area: str -> str
    :param matriz: list -> list
    :return: list -> list'''
    resultado = []
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if area.lower() == matriz[lin][col].lower():
                dados = matriz[lin].copy()
                dados.pop(dados.index(dados[col]))
                resultado.append(dados)

    return resultado