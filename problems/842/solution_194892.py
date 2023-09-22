def pontos_por_time(lista_com_jogo_de_ida_e_jogo_de_volta):
    '''Funcao que retorna um dicionario cujos mapeamentos sao: <nome do time> -> <numero total de pontos na fase>. Os parametros 'jogo_de_ida' e 'jogo_de_volta' sao listas no seguinte formato:
    [TimeVencedor, OutroTime,[Gols_TimeVencedor, Gols_OutroTime]]. Em casos de empate, a ordem dos dois primeiros elementos da lista nao fara diferenca.
    [str,str[int,int]], [str,str[int,int]] -> dict'''

# [    [’Cormengo’,’Flam ́ınthians’, [1, 0]]      ,      [’Flam ́ınthians’, ’Cormengo’, [2, 2]]       ].
#Separei as listas para poder trabalhar melhor com elas durante o código
    jogo_de_ida = lista_com_jogo_de_ida_e_jogo_de_volta[0] 
    jogo_de_volta = lista_com_jogo_de_ida_e_jogo_de_volta[1]
    time1 = jogo_de_ida[0]
    placar1 = jogo_de_ida[1]
    time2 = jogo_de_volta[0]
    placar2 = jogo_de_volta[1]
    pontos_time1 = []
    pontos_time2 = []
    
    if placar1[0]>placar1[1]:
        pontos_time1 = [3]
    if placar1[0]<placar1[1]:
        pontos_time2 = [3]
    else: 
        pontos_time1= [1] 
        pontos_time2= [1]
    
    if placar2[0]>placar2[1]:
        pontos_time1 = [pontos_time1[0] + 3]
    if placar2[0]<placar2[1]:
        pontos_time2 = [pontos_time2[0] + 3]
    else:
       pontos_time1= [pontos_time1[0] + 1]
       pontos_time2= [pontos_time2[0] +1]

    if pontos_time1[0]>=pontos_time2[0]:
        return {'time1': pontos_time1[0], 'time2': pontos_time2[0]}
    else:
        return {'time2': pontos_time2[0], 'time1': pontos_time1[0]}