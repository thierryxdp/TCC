time1 += 0
time2 += 0
time3 += 0
time4 += 0
def pontos_primeiro_jogo(jogos):
   
    if jogos[0][2][0]>jogos[0][2][1]:
        time1 += 3
        time2 += 0
        
    elif jogos[0][2][0]<jogos[0][2][1]:
        time1 += 0
        time2 += 3
        
    elif jogos[0][2][0]==jogos[0][2][1]:
        time1 += 1
        time2 += 1

    return (time1,time2)    

def pontos_segundo_jogo(jogos):

    if jogos[1][2][0]>jogos[1][2][1]:
        time4 += 3
        time3 += 0

    elif jogos[1][2][0]<jogos[1][2][1]:
        time4 += 0
        time3 += 3

    elif jogos[1][2][0]==jogos[1][2][1]:
        time4 += 1
        time3 += 1

    return (time3,time4)


def pontos_por_time(jogos):

    pontos_primeiro_jogo
    pontos_segundo_jogo

    return {jogos[0][0]:(time1+time3),jogos[0][1]:(time2+time4)}