def pontos_por_time(lista):
    '''Retorna um Dicionário com dois times de futebol e seus resultados, dado uma lista com nome dos dois times e seus resultados em dois jogos;
    lista =>lista'''
    jogo1 = lista[0]
    jogo2 = lista[1]
    nome1 = jogo1[0]
    nome2 = jogo1[1]
    nome3 = jogo2[0]
    nome4 = jogo2[1]
    pontos1 = jogo1[2]
    pontos2 = jogo2[2]
    x1 = pontos1[0]
    x2 = pontos1[1]
    y1 = pontos2[0]
    y2 = pontos2[1]

    if x1 > x2:
       a = 3
       b = 0
    if x1 < x2:
       a = 0
       b = 3
    elif x1 == x2:
       a = 1
       b = 1

    elif y1 > y2:
       a2 = 3
       b2 = 0
       
    elif y1 < y2:
       a2 = 0
       b2 = 3
    else:
       a2 = 1
       b2 = 1

    if nome1 == nome3:
        return({nome1:a+a2,nome2:b+b2})
        

    else:
        return({nome1: a+b2,nome2:b+a2})