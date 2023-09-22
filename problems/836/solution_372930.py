def busca(setor, matriz):
    """Retorna os dados de todos os funcionários de um dado setor inscritos numa dada matriz.
    Entrada: 
    Saída: 
    """
    resposta = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            z = matriz[i][:2] + matriz[i][3:]
            list.append(resposta, z)
    return resposta