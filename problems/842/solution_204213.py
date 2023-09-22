def pontos_por_time(jogoi,jogov):
    nome_t1=jogoi[0]
    nome_t2=jogov[0]
    gols_t11=jogoi[2][0]
    gols_t12=+jogov[2][1]
    gols_t21=jogoi[2][1]
    gols_t22=jogov[2][0]
    if gols_t11>gols_t21 or gols_t12>gols_t22 or gols_t21>gols_t11 or gols_t22=gols_t12:
        pontos=3
    elif gols_t11=gols_t21 or gols_t12=gols_t22 or gols_t21=gols_t11 or gols_t22=gols_t12:
        pontos=1
    return nome_t1:pontos,nome_t2:pontos