def pontos_por_time(jogoi, jogov):
    '''função que retorna o número total de gols de cada time
    dadas duas listas dos jogos de ida  e volta
    list, list -> dict'''
    nome_Cormengo=jogoi[0]
    nome_Flam=jogov[0]
    pontos_Cormengo = jogoi[2][0] + jogov[2][1]+1
    pontos_Flam= jogoi[2][1] + jogov[2][0]-1
    return {nome_Cormengo:pontos_Cormengo, nome_Flam:pontos_Flam}