def melhor_volta(matriz):
    '''
    Verifica qual corredor obteve a melhor volta de uma prova, com qual tempo
    e em que volta conseguiu.
    list -> tuple

    Parameters:
    matriz: Parâmetro do tipo lista (list).

    Returns:
    Uma tupla contendo qual corredor obteve a melhor volta, com qual tempo e
    em qual volta.
    '''
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    melhores_tempos = []
    melhor_corredor = 0
    melhor_volta = 0

    if linhas != 6 and colunas != 10:
        return ('Insira uma matriz com 6 linhas e 10 colunas.')
    
    for i in range(linhas):
            list.append(melhores_tempos, (min(matriz[i])))
    
    
    melhor_tempo = min(melhores_tempos)
    melhor_corredor = (melhores_tempos.index(melhor_tempo))
    melhor_volta = (matriz[melhor_corredor].index(melhor_tempo)) + 1
    melhor_corredor = melhor_corredor + 1
    
    campeao = (melhor_corredor, melhor_tempo, melhor_volta)
    return campeao