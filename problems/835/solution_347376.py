def melhor_volta(matriz):
    """
    lista->tupla
    :param matriz: Recebe uma matriz com as informações de cada volta dos corredores
    :param return: Retorna quem foi o melhor da prova
    """
    quantidade_linhas = 6
    quantidade_colunas = 10
    melhores_tempos = []
    for corredor in range(quantidade_linhas):
        tempos = []
        for tempo in range(quantidade_colunas):
            list.append(tempos,matriz[corredor][tempo])
        list.append(melhores_tempos,min(tempos))
    melhor_tempo = min(melhores_tempos)
    melhor_corredor = list.index(melhores_tempos,melhor_tempo)+1
    volta = list.index(matriz[melhor_corredor-1],melhor_tempo)+1
    return melhor_corredor, melhor_tempo, volta