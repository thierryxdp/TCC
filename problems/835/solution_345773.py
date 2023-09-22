def melhor_volta(corrida):
    '''
		Função que retorna uma tupla informando de quem foi a melhor volta da prova, com qual tempo e em que volta.
		Lista => tupla
    '''
    corredor = 0
    melhor_volta = corrida[0].index(min(corrida[0]))
    for i in range(1, len(corrida)):
        v = min(corrida[i])
        if (v < corrida[corredor][melhor_volta]):
            corredor = i
            melhor_volta = corrida[i].index(v)
    return (corredor+1, corrida[corredor][melhor_volta], melhor_volta+1)