def pontos_por_time1(jogo):
    """Retorna um dicionario com os nomes dos times
    e a pontuacao de cada um dado uma lista com
    informacoes do jogo de ida e de volta.
    list -> dict"""
    l1 = jogo
    time1 = l1[0][0]
    time2 = l1[0][1]
    gols_t1_ida = int(l1[0][2][0])
    gols_t1_volta = int(l1[1][2][1])
    gols_t2_ida = int(l1[0][2][1])
    gols_t2_volta = int(l1[1][2][0])
    pontuacao_t1 = ()
    pontuacao_t2 = ()

#condicional para somatorio de pontos do time 1
    
    if gols_t1_ida > gols_t2_ida:
        pontuacao_t1 += (3,)
    if gols_t1_volta > gols_t2_volta:
        pontuacao_t1 += (3,)
    if gols_t1_ida == gols_t2_ida:
        pontuacao_t1 += (1,)
    if gols_t1_volta == gols_t2_volta:
        pontuacao_t1 += (1,)
    if gols_t1_ida < gols_t2_ida:
        pontuacao_t1 += (0,)
    if gols_t1_volta < gols_t2_volta:
        pontuacao_t1 += (0,)

#condicional para somatorio de pontos do time 2
        
    if gols_t2_ida > gols_t1_ida:
        pontuacao_t2 += (3,)
    if gols_t2_volta > gols_t1_volta:
        pontuacao_t2 += (3,)
    if gols_t2_ida == gols_t1_ida:
        pontuacao_t2 += (1,)
    if gols_t2_volta == gols_t1_volta:
        pontuacao_t2 += (1,)
    if gols_t2_ida < gols_t1_ida:
        pontuacao_t2 += (0,)
    if gols_t2_volta < gols_t1_volta:
        pontuacao_t2 += (0,)

    soma_time1 = (pontuacao_t1[0] + pontuacao_t1[1])
    soma_time2 = (pontuacao_t2[0] + pontuacao_t2[1])

    return {time1: soma_time1, time2: soma_time2}