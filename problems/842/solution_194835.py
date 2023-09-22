def pontos_por_time(jogo_de_ida,jogo_de_volta):
    '''Funcao que retorna um dicionario cujos mapeamentos sao: <nome do time> -> <numero total de pontos na fase>. Os parametros 'jogo_de_ida' e 'jogo_de_volta' sao listas no seguinte formato:
    [TimeVencedor, OutroTime,[Gols_TimeVencedor, Gols_OutroTime]]. Em casos de empate, a ordem dos dois primeiros elementos da lista nao fara diferenca.
    [str,str[int,int]], [str,str[int,int]] -> dict'''

#Separei as listas para poder trabalhar melhor com elas durante o código
    jogo_de_ida[0]= times1
    jogo_de_ida[1]= placar1
    jogo_de_volta[0]= times2
    jogo_de_volta[1]= placar2
    pontos_cormengo = []
    pontos_flaminthians = []
    
    if times1[0] == 'Cormengo' and placa1[0]!=placar1[1]:
        pontos_cormengo = [3]
    if times1[0] == 'Flaminthians' and placar[0]!=placar[1]:
        pontos_flaminthians = [3]
    else: pontos_cormengo= [1] and pontos_flaminthians[1]
    
    if times2[0] == 'Cormengo' and placar2[0]!=placar2[1]:
        pontos_cormengo = [pontos_cormengo[0] + 3]
    if times2[0] == 'Flaminthians' and placar2[0]!=placar2[1]:
        pontos_flaminthians = [pontos_flaminthians[0] + 3]
    else:
       pontos_cormengo= [pontos_cormengo[0] + 1], pontos_flaminthians= [pontos_flaminthians[0] +1]
    return {'Cormengo': pontos_cormengo, 'Flaminthians': pontos_flaminthians}