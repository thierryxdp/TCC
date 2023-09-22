def pontos_por_time(lista):
    """Recebe uma lista com dois elementos,  os quais também são listas,
uma referente a primeira partida e outra referente a segunda partida.
Elas contém o nome do primeiro time, do segundo time e o placar de gols
do jogo no formato ["Time1", "Time2" , [gols do time 1, gols do time2]].
Retorna um dicionário que contém os dois times como chaves e os valores
de cada chave são o saldo de pontos o qual consiste em 3 pontos por
vitória, 1 ponto por empate e 0 pontos por derrota.
"""
    dicio = {lista[0][0]:0, lista[0][1]:0}
    gols1 = lista[0][2]
    if gols1[0] < gols1[1]:
        dicio[lista[0][1]] += 3
    elif gols1[0] > gols1[1]:
        dicio[lista[0][0]] += 3
    else:
        dicio[lista[0][0]] += 1
        dicio[lista[0][1]] += 1
        
    gols2 = lista[1][2]
    
    if gols2[0] < gols2[1]:
        dicio[lista[1][1]] += 3
    elif gols2[0] > gols2[1]:
        dicio[lista[1][0]] += 3
    else:
        dicio[lista[1][0]] += 1
        dicio[lista[1][1]] += 1

    return dicio