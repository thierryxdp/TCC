def melhor_volta(matriz):
    '''Função que recebe uma matriz na qual cada linha representa um corredor e cada
    coluna uma volta contendo o tempo do corredor naquela volta, a função retorna
    uma tupla informando qual corredor teve a melhor volta, o tempo e em que volta foi
    o melhor tempo; list -> tuple'''
    linhas = len(matriz)
    colunas = len(matriz[0])
    minTempo = 0
    volta = 0
    resultadoCorredores = []
    minTemposColetivo = []
    for i in range(linhas):
        minTempoIndiv = min(matriz[i])
        volta = matriz[i].index(min(matriz[i]))
        resultadoCorredores += [[i+1, minTempoIndiv, volta+1]]
        minTemposColetivo += [minTempoIndiv]

    menorTempo = minTemposColetivo.index(min(minTemposColetivo))
    result = resultadoCorredores[menorTempo]
    
    return (result[0], result[1], result[2])