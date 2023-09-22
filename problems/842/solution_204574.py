def pontos_por_time(jogoi, jogov):
    '''list, list -> dict'''

    nome_t1=jogoi[0]
    nome_t2=jogov[0]
    pontos_t1 = [jogoi[2][0], jogov[2][1]]
    pontos_t2 = [jogoi[2][1], jogov[2][0]]
    pt_totalv = [3]
    pt_totale = [1]

    if pontos_t1[0] > pontos_t2[0] or pontos_t1[0] < pontos_t2[0] :
        return pt_totalv
    elif pontos_t1[0] == pontos_t2[0]:
        return pt_totale
    elif pontos_t1[1] > pontos_t2[1] or pontos_t1[1] < pontos_t2[1] :
        return pt_totalv+3
    elif pontos_t1[1] == pontos_t2[1]:
        return pt_totale+1