def pontos_por_time(lista): 
    '''Dados duas listas contendo os nomes e os gols de cada time em duas partidas,
       retorna um dicionário cujas chaves são os times e o conteúdo os seus respectivos
       pontos totais.
       [[str, str, list], [str, str, list]] -> {str: int, str: int}'''
    
    pontos_time1 = 0
    pontos_time2 = 0
    gols_time1_ida = lista[0][2][0]
    gols_time1_volta = lista[1][2][1]
    gols_time2_ida = lista[0][2][1]
    gols_time2_volta = lista[1][2][0]
    saldo_ida = gols_time1_ida - gols_time2_ida
    saldo_volta = gols_time1_volta - gols_time2_volta

    if saldo_ida>0:
        pontos_time1 = pontos_time1 + 3
    elif saldo_ida == 0:
        pontos_time1 = pontos_time1 + 1
        pontos_time2 = pontos_time2 + 1
    else:
        pontos_time2 = pontos_time2 + 3

    if saldo_volta>0:
        pontos_time1 = pontos_time1 + 3
    elif saldo_volta == 0:
        pontos_time1 = pontos_time1 + 1
        pontos_time2 = pontos_time2 + 1
    else:
        pontos_time2 = pontos_time2 + 3
    return {lista[0][0]: pontos_time1, lista[0][1]: pontos_time2}