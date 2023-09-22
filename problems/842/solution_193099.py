def pontos_por_time (x):
    """retorna um dicionário com o nome dos times e seus respectivos pontos
que obtiveram"""
    [ [time1,time2,[ponto1,ponto2]] ,[time2,time1,[ponto3,ponto4]] ] = x

    if ponto1 > ponto2 and ponto4 > ponto3:
        p1= + 6
        p2 = 0
    elif ponto2 > ponto1 and ponto3 > ponto4:
        p2 = +6
        p1 = 0
    elif ponto1 == ponto2 and ponto3 == ponto4:
        p1 = +2
        p2 = +2

    return {time1:p1,time2:p2}