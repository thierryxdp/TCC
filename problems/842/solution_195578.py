def pontos_por_time(lista):
    '''Instruções: Indique os dois elementos da lista como listas também.
    Exemplo: [[time1,time2,[gols1,gols2]],[time2,time1,[gols2,gols1]]]'''
#Definição dos times e dos resultados de ida e volta (Separando os dados de entrada)
#t1 e t2: times 1 e 2; r1 e r2: resultados ida e volta; p1 e p2: pontos do time 1 e pontos do time 2
    bloco1 = lista[0]
    bloco2 = lista[1]
    t1 = bloco1[0]
    t2 = bloco1[1]
    r1 = bloco1[2]
    r2 = bloco2[2]
    p1 = 0
    p2 = 0
#Condições de pontuação
#Time 1 ganhou a ida
	if r1[0] > r1[1]:
        p1 = p1 + 3
#Time 1 perdeu a ida
    elif r1[0] < r1[1]:
        p2 = p2 + 3
#empate ida
    elif r1[0] == r1[1]:
        p1 = p1 + 1
        p2 = p2 + 1
#Time 2 ganha volta:
	if r2[0] > r2[1]:
        p2 = p2 + 3
#Time 2 perdeu a ida
    elif r2[0] < r2[1]:
        p1 = p1 + 3
#empate ida
    elif r2[0] == r2[1]:
        p1 = p1 + 1
        p2 = p2 + 1
	dic = {t1:p1,t2:p2}
    return dic