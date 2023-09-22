def pontos_por_time(jogoi, jogov):
    ''' retorna o numero total de pontos de cada time
    dadas duas listas dos jogos de ida  e volta
    list, list -> dict'''

    cormengo = jogoi[0]
    flaminthias = jogov[0]
    pontos_cormengo = jogoi[2][0] + jogov[2][1]
    pontos_flaminthias = jogoi[2][1] + jogov[2][0]
    
    return {cormengo:pontos_cormengo, flaminthias:pontos_flaminthias}