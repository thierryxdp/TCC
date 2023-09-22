def pontos_por_time(jogos):
    """retorna o numero de pontos do time em uma fase"""
    if jogos[0][2][0]>jogos[0][2][1]:
        t1=3
        t2=0
    elif jogos[0][2][0]<jogos[0][2][1]:
        t1=0
        t2=3
    else:
        t1=1
        t2=1
    if jogos[1][2][0]>jogos[1][2][1]:
        t1=t1+0
        t2=t2+3
    elif jogos[1][2][0]<jogos[1][2][1]:
        t1=t1+3
        t2=t2+0
    else:
        t1=t1+1
        t2=t2+1
    return {jogos[0][0]:t1, jogos[0][1]:t2}