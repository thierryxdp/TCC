def pontos_por_time (lista):
    '''Funcao que, dada uma lista tendo como elementos dois elementos ['time1',
    'time2', [time1j1, time2j2], ['time2', 'time1', [time2j2, time1j2]],
    retorna um dicionario com os times e seus respectivos pontos;
    entrada: list
    saida: dict'''

    time1 = lista[0][0]
    time2 = lista[0][1]
    time1j1 = lista[0][2][0]
    time2j1 = lista[0][2][1]
    time2j2 = lista[1][2][0]
    time1j2 = lista[1][2][1]
    pontotime1=0
    pontotime2=0
#jogo 1:
    if time1j1 > time2j1 :
        pontotime1 += 3
    elif time1j1 == time2j1:
            pontotime2 += 1
            pontotime1 += 1
    elif time1j1 < time2j1:
            pontotime2 += 3
#jogo 2:
    if time1j2 > time2j2:
        pontotime1 += 3
    elif time1j2 == time2j2:
            pontotime2 += 1
            pontotime1 += 1
    elif time1j2 < time2j2:
            pontotime2 += 3
    dicionario = {time1:pontotime1, time2:pontotime2}
    return dicionario