def pontos_por_time(x):
    """Função que recebe uma lista de dois elementos, onde cada um desses elementos é também uma lista,
que contém informações do número de gols em dois jogos de futebol entre dois times, e retorna um dicionário
cujos mapeamentos são:<nome do time> → <numero de pontos na fase>.
list->dict"""
    
    if x[0][2][0]==x[0][2][1]:
        a=1
        b=1
        
    if x[0][2][0]>x[0][2][1]:
        a=3
        b=0
        
    if x[0][2][0]<x[0][2][1]:
        a=0
        b=3

    if x[1][2][0]==x[1][2][1]:
        c=1
        d=1

    if x[1][2][0]>x[1][2][1]:
        c=3
        d=0

    if x[1][2][0]<x[1][2][1]:
        c=0
        d=3
    dic={x[0][0]:(a), x[0][1]:(b)}
    dic2={x[1][0]:(b+c), x[1][1]:(a+d)}
    return dic2