def pontos_por_time(lista):
    '''função que recebe uma lista de dois elementos, onde cada elemento é também uma lista.A lista completa tem o número de gols do jogo da ida e jogo da volta, no seguinte formato[[time1,time2,[pontotime1,pontotime2]],[time2,time1,[pontotime2,pontotime1]]].Nesse sentido, a função retorna um dicionario cujo mapeamento é o nome do time e o número total de pontos na fase.Observando que cada vitoria vale 3 pontos,empate vale 1 ponto e derrota 0 pontos; list -> dictionary'''
    time1=lista[0][0]
    time2=lista[0][1]
    pontos_time_1=0
    pontos_time_2=0
    gols_time1_p1=lista[0][2][0]
    gols_time1_p2=lista[1][2][1]
    gols_time2_p1=lista[0][2][1]
    gols_time2_p2=lista[1][2][0]
    if gols_time1_p1>gols_time2_p1:
        pontos_time_1+=3
    if gols_time2_p1>gols_time1_p1:
        pontos_time_2+=3
    if gols_time2_p1==gols_time1_p1:
        pontos_time_2+=1
        pontos_time_1+=1
    if gols_time1_p2>gols_time2_p2:
        pontos_time_1+=3
    if gols_time2_p2>gols_time1_p2:
        pontos_time_2+=3
    if gols_time2_p2==gols_time1_p2:
        pontos_time_2+=1
        pontos_time_1+=1
    return {time1:pontos_time_1,time2:pontos_time_2}