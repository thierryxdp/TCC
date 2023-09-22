def pontos_por_time(jogo_ida, jogo_volta):
    '''Função que calcula e retorna o número de pontos de dois times, 3 pontos por vitoria, 1 ponto por empate e nenhum por derrota. 
    list, list ->dicionario'''    
    gols = jogo_ida[2]
    ji = jogo_ida
    jv = jogo_volta    
    pts = []
    if gols[0]>gols[1]:
        pts={ji[0]: 3, ji[1]: 0}
    elif gols[0]<gols[1]:
        pts={ji[0]: 0, ji[1]: 3}
    elif gols[0]==gols[1]:
        pts={ji[0]: 1, ji[1]: 1}
    elif gols[0]>gols[1]:
        pts={jv[0]: 3, jv[1]: 0}
    elif gols[0]<gols[1]:
        pts={jv[0]: 0, jv[1]: 3}
    elif gols[0]==gols[1]:
        pts={jv[0]: 1, jv[1]: 1}
    return pts