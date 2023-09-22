def pontos_por_time(lista):
    '''a partir de uma lista composta por duas listas, uma contendo um jogo de ida e outra contendo um jogo de volta entre dois times, retorna a quantidade de pontos conquistada por cada um
    list-->dictionary'''
    primeiro_time=lista[0][0]
    segundo_time=lista[0][1]
    gols1=lista[0][2]
    gols2=lista[1][2]
    if gols1[0]>gols1[1]:
        pontos1=3
        pontos2=0
    elif gols1[1]>gols1[0]:
        pontos1=0
        pontos2=3
    elif gols_ida[0]==gols_ida[1]:
        pontos1=1
        pontos2=1
    elif gols2[0]>gols2[1]:
        pontos1=pontos1+3
    elif gols2[1]>gols2[0]:
        pontos2=pontos2+3
    elif gols2[0]==gols2[1]:
        pontos1=pontos1+1 
        pontos2=pontos2+1
    return {primeiro_time:pontos1,segundo_time:pontos2}