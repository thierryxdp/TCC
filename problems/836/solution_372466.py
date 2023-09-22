def busca(area, matriz):
    '''Busca por usuário com base na área de atuação.
    str, list -> list'''
    result = []
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if area.lower() == matriz[linha][coluna].lower():
                dados = matriz[linha].copy()
                dados.pop(dados.index(dados[coluna]))
                result.append(dados)

    return result