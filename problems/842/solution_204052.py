def pontos_por_time(lista):
    '''Retorna um dicionário cujos mapeamentos são <nome do time> -> <número total de pontos na fase>
    a partir de uma lista cujos elementos são a lista1=['time1','time2',resultado] e a lista2=['time2',
    'time1',resultado]'''
    nome1=lista[0][0]
    gols1=lista[0][2][0]
    gols2=lista[0][2][1]
    gols3=lista[1][2][0]
    gols4=lista[1][2][1]
    if gols1<gols2:
        Pontos1=0
    elif gols1==gols2:
        Pontos1=1
    else:
        Pontos1=3
    if gols3>gols4:
        Pontos2=0
    elif gols3==gols4:
        Pontos2=1
    else:
        Pontos2=3
    nome2=lista[0][1]
    if gols1>gols2:
        Pontos3=0
    elif gols1==gols2:
        Pontos3=1
    else:
        Pontos3=3
    if gols3<gols4:
        Pontos4=0
    elif gols3==gols4:
        Pontos4=1
    else:
        Pontos4=3
    return {nome1:Pontos1+Pontos2,nome2:Pontos3+Pontos4}