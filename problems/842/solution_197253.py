def pontos_por_time(lista_gols):
# lista_gols = [[<nome time1>,<nome time2>,[<gols time1 jogo1>,<gols time2 jogo1>]],[<nome time2>,<nome time1>,[<gols time1 jogo2>,<gols time2 jogo2>]]]
    '''
        Funcao recebe uma lista com duas listas referentes ao numero de gols
        do primero e do segundo jogo, respectivamente, entre dois times e
        retorna um dicionario com o nome dos times e seus respectivos numeros
        de pontos na fase
        list -> dicio
        
    '''
    time1 = lista_gols[0][0]
    time2 = lista_gols[0][1]
    j1golsT1 = lista_gols[0][2][0]
    j1golsT2 = lista_gols[0][2][1]
    j2golsT1 = lista_gols[1][2][0]
    j2golsT2 = lista_gols[1][2][1]

    if (j1golsT1 > j1golsT2) and (j2golsT1 > j2golsT2):
        return {time1:6,time2:0}
    if (j1golsT1 < j1golsT2) and (j2golsT1 < j2golsT2):
        return {time1:0,time2:6}
    if (j1golsT1 > j1golsT2 and j2golsT1 < j2golsT2) or (j1golsT1 < j1golsT2 and j2golsT1 > j2golsT2):
        return {time1:3,time2:3}
    if (j1golsT1 == j1golsT2 and j2golsT1 > j2golsT2) or (j1golsT1 > j1golsT2 and j2golsT1 == j2golsT2):
        return {time1:4,time2:1}
    if (j1golsT1 == j1golsT2 and j2golsT1 < j2golsT2) or (j1golsT1 < j1golsT2 and j2golsT1 == j2golsT2):
        return {time1:1,time2:4}
    else:
        return {time1:2,time2:2}