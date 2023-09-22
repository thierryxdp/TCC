def busca(string, matriz):
    """Função que recebe uma matriz contendo os dados dos funcionários de uma empresa e nos retorna os dados de todos os funcionários pertencentes ao setor correspondente
    str, list -> list """

    matriz_setor = []

    for i in range(len(matriz)):
            if string == matriz[i][2]:
                matriz_setor.append(matriz[i])
                del matriz_setor[2]
                

    return matriz_setor