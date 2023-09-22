def busca(setor, matriz):
    """Retorna os dados de todos os funcionários de um dado setor inscritos numa dada matriz.
    Entrada: 
    Saída: 
    """
    resposta = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            list.append(resposta, matriz[i])
    return resposta