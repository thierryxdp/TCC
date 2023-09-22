def pontos_por_time(lista):
    '''a partir de uma lista composta por duas listas, uma contendo um jogo de ida e outra contendo um jogo de volta entre dois times, retorna a quantidade de pontos conquistada por cada um
    list-->dictionary'''
    ida=lista[0]
    volta=lista[1]
    times_ida=ida[0:2]
    gols_ida=ida[2:]
    times_volta=volta[0:2]
    gols_volta=volta[2:]
    pontos1=()
    pontos2=()
    if gols_ida[0]>gols_ida[1]:
        pontos1=pontos1+3
    elif gols_ida[0]<gols_ida[1]:
        pontos2=pontos2+3
    elif gols_ida[0]==gols_ida[1]:
        pontos1=pontos1+1 
        pontos2=pontos2+1
    elif gols_volta[0]>gols_volta[1]:
        pontos1=pontos1+3
    elif gols_volta[0]<gols_volta[1]:
        pontos2=pontos2+3
    elif gols_volta[0]==gols_volta[1]:
        pontos1=pontos1+1 
        pontos2=pontos2+1
    return {times_ida[0]:pontos1,times_ida[1]:pontos2}