def pontos_por_time (jogos) :
    '''Função que recebe nomes de times e seus gols nos seus
    jogos de ida e volta em formato de lista, retornando um
     dicionário contendo o numero de pontos atribuídos a cada
     time. A entrada jogos corresponde aos resultados de ida 
     e volta, time1 e time2 às entradas da lista jogos que 
     correspondem aos nomes dos times. No primeiro teste,
     são atribuidas às entradas pontotime1 e pontotime2 os 
     valores dos pontos dos time dependendo dos resultados
     inseridos na lista jogos. No segundo teste, são somados
     à essas entradas outros valores dependendo do resultado
     de volta da lista jogos'''
    time1 = jogos[0][0]
    time2 = jogos[0][1]
    if jogos[0][2][0] > jogos[0][2][1]:
        pontotime1 = 3
        pontotime2 = 0
    elif jogos[0][2][0] == jogos[0][2][1]:
        pontotime1 = 1
        pontotime2 = 1
    else:
        pontotime1 = 0
        pontotime2 = 3
    if jogos[1][2][0] > jogos[1][2][1]:
        pontotime2 += 3
    elif jogos[1][2][0] == jogos[1][2][1]:
        pontotime1 += 1
        pontotime2 += 1
    else:
        pontotime1 += 3
    return ({time1:pontotime1,time2:pontotime2})