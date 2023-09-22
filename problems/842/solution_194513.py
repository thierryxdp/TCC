def pontos_por_time(lista):
    """funcao que dado de entrada uma lista com informações 
    do numero de gols em dois jogos de futebol entre dois 
    times, retorna um dicionario mapeando o nome dos
    times e o total de pontos na fase de cada um; 
    Essa lista deve possuir dois elementos, onde o primeiro 
    elemento é uma lista sobre os dados do jogo 1, e o 
    segundo é uma outra lista sobre os dados do jogo 2, que
    deverá ser escrita da seguinte forma:
    [['Time1','Time2',[gols_time1,gols_time2]],['Time2','Time1',[gols_time2,gols_time1]]];
    list -> dict"""	
    jogo1 = lista[0]
    gols1 = jogo1[2]
    jogo2 = lista[1]
    gols2 = jogo2[2]
    'time1' == jogo1[0]
    'time2' == jogo1[1]
    dicionario = {'time1':0,'time2':0}
    if gols1[0] > gols1[1]:
        dicionario['time1'] += 3 
    if gols2[1]>gols2[0]:
        dicionario['time1'] += 3
    if gols1[0] < gols1[1]:
        dicionario['time2'] += 3
    if gols2[1]<gols2[0]:
        dicionario ['time2'] += 3
    if gols1[0] == gols1[1]:
        dicionario ['time1'] += 1
        dicionario ['time2'] += 1
    if gols2[1]== gols2[0]:
        dicionario ['time1'] += 1
        dicionario ['time2'] += 1
    return dicionario