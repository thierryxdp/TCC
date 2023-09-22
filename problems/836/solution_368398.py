def busca(string, matriz):
    """Função que recebe uma matriz contendo os dados dos funcionários de uma empresa e nos retorna os dados de todos os funcionários pertencentes ao setor correspondente
    str, list -> list """

    matriz_setor = []

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if string == matriz[i][2]:
                matriz_setor.append(matriz[i])
            

    return matriz_setor