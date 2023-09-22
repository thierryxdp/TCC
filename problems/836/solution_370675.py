def busca(setor, matriz):
    """ Dada um setor e uma matriz de funcionários de uma empresa, retorna todos os funcionários que pertencem aquele setor.
    string, list -> list
    """
    resultado = []
    for i in range(len(matriz)):
        for j in matriz[i]:
            if(setor == j):
                resultado.append([matriz[i][0], matriz[i][1], matriz[i][3]])
    return resultado