def busca(setor, matriz):
    """Retorna os dados de todos os funcionários em uma matriz
    Entrada: 
    Saída: 
    """
    banco = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            posicao = matriz[i][:2] + matriz[i][3:]
            list.append(banco,posicao)
    return banco