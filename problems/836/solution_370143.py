def busca(setor,matriz_dados):
    """função que retorna os dados de todos os funcionários de um determinado setor da empresa,
    através dos dados de entrada setor e matriz_dados,
    Entrada: str, list
    Saída: list"""
    x = 0
    resultado = []
    
    for x in range(len(matriz_dados)):
        if setor in matriz_dados[x]:
            del matriz_dados[x][2]
            resultado = resultado + [matriz[x]]
        resultado = resultado + 1
    return resultado