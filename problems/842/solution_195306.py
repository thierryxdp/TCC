def pontos_por_time(lista_com_jogo_de_ida_e_jogo_de_volta):
    '''Funcao que retorna um dicionario cujos mapeamentos sao: <nome do time> -> <numero total de pontos na fase>. Os parametros 'jogo_de_ida' e 'jogo_de_volta' sao listas no seguinte formato:
    [TimeVencedor, OutroTime,[Gols_TimeVencedor, Gols_OutroTime]]. Em casos de empate, a ordem dos dois primeiros elementos da lista nao fara diferenca.
    [str,str[int,int]], [str,str[int,int]] -> dict'''

#Separei as listas para poder trabalhar melhor com elas durante o código
    jogo_de_ida = lista_com_jogo_de_ida_e_jogo_de_volta[0] 
    jogo_de_volta = lista_com_jogo_de_ida_e_jogo_de_volta[1]
    times = jogo_de_ida[0:2]
    placar1 = jogo_de_ida[2]
    placar2 = jogo_de_volta[2]
    pontos_time1 = []
    pontos_time2 = []
    
    if placar1[0]>placar1[1]:
        pontos_time1 = [3,0]
    if placar1[0]<placar1[1]:
        pontos_time1 = [0,3]
    else: 
        pontos_time1= [1,1]
    
    if placar2[0]>placar2[1]:
        pontos_time2 = [3,0]
    if placar2[0]<placar2[1]:
        pontos_time2 = [0,3]
    else:
        pontos_time2= [1,1]

    pontos_totais = (pontos_time1[0] + pontos_time2[1]), (pontos_time1[1] + pontos_time2[0])
    placar = {times[0]: pontos_totais[0], times[1]: pontos_totais[1]}

    return placar#Start your python function here