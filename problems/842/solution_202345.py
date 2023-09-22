#Start your python function here
def pontos_por_time(l):
    '''Recebe como parâmetro uma lista contendo os times e o placar de cada jogo por elemento, com dois elementos no total, no formato [['Cormengo', 'Flamınthians', [1, 0]], ['Flamınthians', 'Cormengo', [2, 2]]]. Em cada jogo, os times recebem três pontos por vitória e um ponto por empate. Derrotas não implicam perda de pontos. pontos_por_time calcula os pontos de cada time na fase e retorna o nome do time e seus respectivos números de pontos na fase em um formato de dicionário, cujas chaves são os nomes dos times e cujos valores são os respectivos pontos de cada time. O total de pontos de cada time em uma
fase é a soma de pontos do time nos dois jogos da fase;
    assinatura: list --> dict{string: int, string: int}
    Casos de teste:
    pontos_por_time([['Cormengo', 'Flamınthians', [1, 0]], ['Flamınthians', 'Cormengo', [2, 2]]]) == {'Cormengo': 4, 'Flamınthians': 1}
    pontos_por_time([['Cormengo', 'Flamınthians', [0, 1]], ['Flamınthians', 'Cormengo', [3, 2]]]) == {'Cormengo': 0, 'Flamınthians': 6}
    pontos_por_time([['Cormengo', 'Flamınthians', [0, 1]], ['Flamınthians', 'Cormengo', [2, 3]]]) == {'Cormengo': 3, 'Flamınthians': 3}
    pontos_por_time([['Cormengo', 'Flamınthians', [1, 1]], ['Flamınthians', 'Cormengo', [0, 0]]]) == {'Cormengo': 2, 'Flamınthians': 2}
    '''
    time1 = l[0][0]
    time2 = l[0][1]
    gols_time1_jogo1 = l[0][2][0]
    gols_time2_jogo1 = l[0][2][1]
    gols_time1_jogo2 = l[1][2][1]
    gols_time2_jogo2 = l[1][2][0]
    pontos_time1 = 0
    pontos_time2 = 0
    
    if gols_time1_jogo1 > gols_time2_jogo1:
        pontos_time1 += 3
    elif gols_time1_jogo1 == gols_time2_jogo1:
        pontos_time1 += 1
        pontos_time2 += 1
    elif gols_time2_jogo1 > gols_time1_jogo1:
        pontos_time2 += 3
    
    if gols_time1_jogo2 > gols_time2_jogo2:
        pontos_time1 += 3
    elif gols_time1_jogo2 == gols_time2_jogo2:
        pontos_time1 += 1
        pontos_time2 += 1
    elif gols_time2_jogo2 > gols_time1_jogo2:
        pontos_time2 += 3
        
    return {time1: pontos_time1, time2: pontos_time2}