def pontos_por_time(jogos):
    nome_time=jogos[0][0] or jogos [1][0]
    if jogos[0][2][0]>jogos[0][2][1] and jogos[1][2][1]>jogos[1][2][0]:
        return {nome_time:0, nome_time:6}
    elif jogos[0][2][0]<jogos[0][2][1] and jogos[1][2][1]<jogos[1][2][0]:
        return {nome_time:6, nome_time:0}
    elif jogos[0][2][0]<jogos[0][2][1] and jogos[1][2][1]>jogos[1][2][0]:
        return {nome_time:3, nome_time:3}
    elif jogos[0][2][0]>jogos[1][2][0] and jogos[0][2][1]<jogos[1][2][1]:
        return {nome_time:3, nome_time:3}
    elif jogos[0][2][0]==jogos[0][2][1] and jogos[1][2][1]>jogos[1][2][0]:
        return {nome_time:4, nome_time:1}
    elif jogos[0][2][0]==jogos[0][2][1] and jogos[1][2][1]<jogos[1][2][0]:
        return {nome_time:1, nome_time:4}
    elif jogos[0][2][0]>jogos[0][2][1] and jogos[1][2][1]==jogos[1][2][0]:
        return {nome_time:4, nome_time:1}
    elif jogos[0][2][0]<jogos[0][2][1] and jogos[1][2][1]==jogos[1][2][0]:
        return {nome_time:1, nome_time:4}
    else:
        return {nome_time:2, nome_time:2}