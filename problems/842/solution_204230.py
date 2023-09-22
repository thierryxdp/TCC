def pontos_por_time(jogoi,jogov):
    nome_t1=jogoi[0]
    nome_t2=jogov[0]
    gols_t11=jogoi[2][0]
    gols_t12=jogov[2][1]
    gols_t21=jogoi[2][1]
    gols_t22=jogov[2][0]
    if gols_t11>gols_t21 and gols_t12>gols_t22:
        return {nome_t2:0, nome_t1:6}
    elif gols_t11>gols_t21 and gols_t12==gols_t22 or gols_t11==gols_t21 and gols_t12>gols:
        return {nome_t2:1, nome_t1:4}
    elif gols_t11<gols_t21 and gols_t12<gols_t22:
        return {nome_t2:6, nome_t1:0, }
    elif gols_t11<gols_t21 and gols_t12==gols_t22 or gols_t11==gols_t21 and gols_t12<gols_t22:
        return {nome_t2:4,nome_t1:1}