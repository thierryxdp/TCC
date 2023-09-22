def busca(matriz, setor):
    '''
    	Funcao que recebe uma matriz e faz uma busca por setor
        e retorna os dados de todos os funcionarios daquele
        setor
        list, setor -> list
    '''
    dados = []
    qtd_linhas = len(matriz)
    for i in range(qtd_linhas):
        if setor in matriz[i]:
            dados.append(matriz[i])
            for j in range(len(dados)):
                if dados[j][2] == setor:
                    del dados[j][2]
    return dados