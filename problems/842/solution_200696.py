def pontos_por_time(resultados):
    '''
    funcao que recebe uma lista de dois parâmetros, que tambem sao listas
    de informacoes sobre os resultados de dois jogos entre dois times. A funcao
    deve retornar um dicionario com mapeamentos que contem o nome do time
    e o numero total de pontos do respectivo time. O total de pontos e calculado
    atraves dos resultados dos dois jogos por meio da seguinte forma: cada
    vitoria resulta em tres pontos para o time vencedor e zero pontos para
    perdedor, ja em caso de empate ambos os times recem um ponto.
    '''
    lista0 = resultados[0]
    lista1 = resultados[1]
    gols0 = lista0[2]
    gols1 = lista1[2]
    
    if str(lista0[0]) == str(lista1[0]):
        if gols0[0] > gols0[1] and gols1[0] > gols1[1]:
            return {lista0[0] : 6, lista0[1] : 0}
        
        elif gols0[0] > gols0[1] and gols1[0] < gols1[1]:
            return {lista0[0] : 3, lista0[1] : 3}
        
        elif gols0[0] < gols0[1] and gols1[0] < gols1[1]:
            return {lista0[0] : 0, lista0[1] : 6}
        
        elif gols0[0] == gols0[1] and gols1[0] == gols1[1]:
            return {lista0[0] : 2, lista0[1] : 2}
        
        elif gols0[0] > gols0[1] and gols1[0] == gols1[1]:
            return {lista0[0] : 4, lista0[1] : 1}
        
        elif gols0[0] == gols0[1] and gols1[0] > gols1[1]:
            return {lista0[0] : 4, lista0[1] : 1}
        
        elif gols0[0] == gols0[1] and gols1[0] < gols1[1]:
            return {lista0[0] : 1, lista0[1] : 4}
        
        elif gols01[0] < gols0[1] and gols1[0] > gols1[1]:
            return {lista0[0] : 3, lista0[1] : 3}
        
        elif gols0[0] < gols0[1] and gols1[0] == gols1[1]:
            return {lista0[0] : 1, lista0[1] : 4}

        
    elif str(lista0[0]) != str(lista1[0]):
        if gols0[0] > gols0[1] and gols1[0] > gols1[1]:
            return {lista0[0] : 3, lista0[1] : 3}
        
        elif gols0[0] > gols0[1] and gols1[0] < gols1[1]:
            return {lista0[0] : 6, lista0[1] : 0}
        
        elif gols0[0] < gols0[1] and gols1[0] < gols1[1]:
            return {lista0[0] : 3, lista0[1] : 3}
        
        elif gols0[0] == gols0[1] and gols1[0] == gols1[1]:
            return {lista0[0] : 2, lista0[1] : 2}
        
        elif gols0[0] > gols0[1] and gols1[0] == gols1[1]:
            return {lista0[0] : 4, lista0[1] : 1}
        
        elif gols0[0] == gols0[1] and gols1[0] > gols1[1]:
            return {lista0[0] : 1, lista0[1] : 4}
        
        elif gols0[0] == gols0[1] and gols1[0] < gols1[1]:
            return {lista0[0] : 4, lista0[1] : 1}
        
        elif gols0[0] < gols0[1] and gols1[0] > gols1[1]:
            return {lista0[1] : 6, lista0[0] : 0}
        
        elif gols0[0] < gols0[1] and gols1[0] == gols1[1]:
            return {lista0[0] : 1, lista0[1] : 4}