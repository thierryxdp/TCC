def busca(setor,matriz):
    """Função que lista funcionários de um setor dado o setor e a matriz"""
    """String, List -> List"""
    resultado = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            resultado.append([matriz[i][0],matriz[i][1],matriz[i][3]])
    return resultado