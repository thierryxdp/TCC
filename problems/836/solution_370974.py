def busca(setor: str, matriz: list) -> list:
    """Essa função, dada uma matriz com os dados dos funcionários 
    de uma empresa e o nome de um setor como parâmetros de entrada,
    retorna os dados de todos os funcionários daquele setor"""
    
    dados = []
    
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
                del(matriz[i][2])
                dados.append(matriz[i])
    return dados