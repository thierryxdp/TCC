def pontos_por_time (lista):
    '''Instruções: Os dois elementos da lista, são também listas, veja o exemplo de como inserir o valor:
    Exemplo: [[time1,time2,[gols1,gols2]],[time2,time1,[gols2,gols1]]]'''
#Definindo times
t = lista[0:1]
time1 = t[0:1]
time2 = t[1:]
#Definindo o resultado de cada partida
    p1 = lista[0:1]
    result_1 = p1[2:]
    p2 = lista[1:]
    result_2 = p2[2:]
#Condições de pontuação
#Cormengo ganha ida
    if result_1[0:1] > result_1[1:]:
        pontos_t1 = 3
#Cormengo perde ida
    if result_1[0:1] < result_1[1:]:
        pontos_t2 = 3
#Empate ida
    if result_1[0:1] == result_1[1:]:
        pontos_t1 = 1
        pontos_t2 = 1
#Flaminthians ganha volta
    if result_2[0:1] > result_2[1:]:
        pontos_t1 = 3
#Flaminthians perde volta
    if result_2[0:1] < result_2[1:]:
        pontos_t2 = 3
#Empate volta
    if result_2[0:1] == result_2[1:]:
        pontos_t1 = 1
        pontos_t2 = 1
    dic = {time1:pontos_t1, time2:pontos_t2}
    return dic