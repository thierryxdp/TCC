def pontos_por_time(jogos):

    l1 = jogos[0]

    l2 = jogos[1]

    time1 = l1[0]

    time2 = l1[1]

    pontos = [0, 0] # cormengo, flaminthians

    

    # jogo de ida

    if(l1[0] == time1):

       if(l1[2][0] > l1[2][1]): # vitoria

       		pontos[0] = 3

       elif(l1[2][0] == l1[2][1]): # empate

        	pontos[0] = 1

            pontos[1] = 1

       else:

            pontos[1] = 3

    

    # jogo de volta

    if(l2[0] == time1):

       if(l2[2][0] > l2[2][1]): # vitoria

       		pontos[0] = pontos[0] + 3

       elif(l2[2][0] == l2[2][1]): # empate

        	pontos[0] = pontos[0] + 1

            pontos[1] = pontos[1] + 1

       else:

        	pontos[1] = pontos[1] + 3

    

    if(l2[0] == time2):

       if(l2[2][0] > l2[2][1]): # vitoria

       		pontos[1] = pontos[1] + 3

       elif(l2[2][0] == l2[2][1]): # empate

        	pontos[1] = pontos[1] + 1

            pontos[0] = pontos[0] + 1

       else:

        	pontos[0] = pontos[0] + 3

    

    return {time1 : pontos[0], time2 : pontos[1]}