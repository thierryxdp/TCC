def pontos_por_time(jogos):
    ''' Função que calcula os pontos dos times em um capeonato, essa função tera 2 elementos, onde cada elemento também é uma lista,
    a função vai retoranar um dicionário, list-list->dicionário'''

    jogo1=jogos[0]
    jogo2=jogos[1]
    
    time1= jogo1[2][0]
    time2= jogo1[2][1]
    time1j2= jogo2[2][1]
    time2j2= jogo2[2][0]
    pontos1= 0
    pontos2= 0
    if time1 > time2:
        pontos1 = 3
    elif time2 > time1:
        pontos2 = 3
    if time1j2 > time2j2:
        pontos1 += 3
    elif time2j2 > time1j2:
        pontos2 +=3
    if time1 == time2:
        pontos1 = 1
        pontos2 = 1
    elif time1j2 == time2j2:
        pontos1 += 1
        pontos2 += 1
      
    return {jogo1[0]:pontos1,jogo1[1]:pontos2}#Start your python function here