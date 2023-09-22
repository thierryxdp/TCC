def pontos_por_time (x):
    """retorna um dicionário com o nome dos times e seus respectivos pontos
que obtiveram"""
    [ [time1,time2,[ponto1,ponto2]] ,[time2,time1,[ponto3,ponto4]] ] = x
    if ponto1 > ponto2:
        p1= + 3
        p2= 0
    elif ponto4 > ponto3:
        p3 = + 3
        p4 = 0
    elif ponto2 > ponto1:
        p2 = + 3
        p1 = 0
    elif ponto3 > ponto4:
        p3 = + 3
        p4 = 0
    elif ponto1 == ponto2:
        p1 = +1
        p2 = +1
    elif ponto3 == ponto4:
        p3 = +1
        p4 = +1
    p1 + p4 = pontofinal1
    p2 + p3 = pontofinal2
    return {time1:pontofinal1,time2:pontofinal2}