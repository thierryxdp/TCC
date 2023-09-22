def busca (setor, matriz):
    """Funcao que receba uma matriz e faz uma busca dado setor que retorna os dados de todos os funcionarios daquele setor"""
    matriz_f = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            matriz.append(matriz_f, matriz[i][0])
            matriz.append(matriz_f, matriz[i][1])
            matriz.append(matriz_f, matriz[i][3])
    return matriz_f