def melhor_volta(matriz: list) -> tuple:
    """ DADO UMA MATRIZ NO FORMATO LISTA,
    COM AS INFORMAÇÕES DE UMA CORRIDA DE KART,
    RETORNA UMA TUPLA COM AS INFORMAÇÕES DE QUEM DEU A MELHOR VOLTA,
    O MELHOR TEMPO E EM QUAL VOLTA, RESPECTIVAMENTE """
    
    minimos = []
    linhas = len(matriz)
    colunas = len(matriz[0])
    i = 0
    
    """ CRIA A LISTA 'MINIMOS' QUE POSSUI OS MELHORES RESULTADOS """
    while i < linhas:
        minimos += [min(matriz[i]),]
        i += 1
        
    """ INFORMAÇOES """   
    melhor_jogador = list.index(minimos, min(minimos)) + 1
    melhor_tempo = min(minimos)
    melhor_partida = list.index(matriz[list.index(minimos, min(minimos))], min(minimos)) + 1

    return tuple([melhor_jogador,] + [melhor_tempo,] + [melhor_partida,])