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

    if linhas != 6 or colunas != 10:
        return ('Insira uma matriz com 6 linhas e 10 colunas.')
    
    for i in range(linhas):
        for j in range(colunas):
            tempos = matriz[i]
            for tempo in tempos:
                if matriz[i][j] < matriz[0][0]:
                    melhor_tempo = matriz[i][j]
                    melhor_corredor = i + 1
                    melhor_volta = j + 1
                        
    campeao = (melhor_corredor, melhor_tempo, melhor_volta)
    return campeao