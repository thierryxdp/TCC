def melhor_volta(matriz):
    """recebe como entrada uma matriz 6x10 com os tempos em segundos dos corredores em cada volta
    e retorna uma tupla informando de quem foi a melhor volta, com o tempo e em que volta
    6 linhas e 10 colunas"""
    melhores_tempos = []
    melhores_voltas = []
    
    for tempo_corredor in matriz:
        
        crescente = []
        crescente = crescente + tempo_corredor
        list.sort(crescente)
        melhor_tempo = crescente[-1]
        volta = 1
        
        for voltas in tempo_corredor:
            if voltas != melhor_tempo:
                volta = volta + 1
            if voltas == melhor_tempo:
                break

        melhores_tempos = melhores_tempos + [melhor_tempo]
        melhores_voltas = melhores_voltas + [volta]

    tempo_melhor = max(melhores_tempos)
    melhor_corredor = list.index(melhores_tempos,tempo_melhor)
    volta_tempo = melhores_voltas[melhor_corredor]
    
    return (melhor_corredor + 1), tempo_melhor, volta_tempo