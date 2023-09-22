def pontos_por_time(l):
    """ Recebe uma lista de dois elementos, onde cada um desses elementos  ́e também uma lista. 
    A lista completa tem informações do número de gols em dois jogos de futebol entre dois 
    times (jogo da ida e jogo da volta), no seguinte formato: [[’Cormengo’, ’Flam ́ıntians’, 
    [1, 0]], ’Flamíntians’, ’Cormengo’, [2, 2]]]. Nesta lista de exemplo, no primeiro jogo
    entre Cormengo e Flamíntians, o Cormengo fez 1 gol e o Flamíntians não fez
    gol. Retorna um dicionário cujos mapeamentos são:<nome do time>→<numero de pontos na fase>. 
    Os pontos de um time na fase são calcula-dos da seguinte forma: em cada jogo, os times recebem 
    três pontos por vitória e um ponto por empate. Não são atribuídos pontos para derrotas. O total 
    list -> dict"""
    gols = l[0][2]+l[1][2]
    timeA = l[0][0]
    timeB = l[0][1]
    if gols[0]== gols[1] and gols[3]==gols[2]:
        return {timeA:2,timeB:2}
    if gols[0] > gols[1] and gols[3] > gols[2]:
        return {timeA:6,timeB:0}
    if gols[0] < gols[1] and gols[3] < gols[2]:
        return {timeB:6,timeA:0}
    if gols[0] > gols[1] and gols[3]==gols[2]:
        return {timeA:4,timeB:1}
    if gols[0] < gols[1] and gols[3]==gols[2]:
        return {timeB:4,timeA:1}
    if gols[0] < gols[1] and gols[3] > gols[2]:
        return {timeA:3,timeB:3}
    if gols[0] > gols[1] and gols[3] < gols[2]:
        return {timeA:3,timeB:3}