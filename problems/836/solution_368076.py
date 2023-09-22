def busca(area, matriz):
    """Dado um nome de um setor da empresa, retorna os dados de todos os
    funcionários daquele setor."""
    resultado = []
    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz[linha])):
            if area.lower() == matriz[linha][coluna].lower():
                dados = matriz[linha].copy()
                dados.pop(dados.index(dados[coluna]))
                resultado.append(dados)

    return resultado