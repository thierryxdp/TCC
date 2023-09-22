def pontos_por_time(jogos):
    """ao que recebe uma lista com dois elementos e retorna um dicionario cujos mapeamentos sao nome do time e numero total de pontos.
    list, list -> list"""
    l1 = jogos[0]
    l2 = jogos[1]
    time1 = l1[0]
    time2 = l1[1]
    pontos = [0,0]
    if(l1[0] == time1):
        if(l1[2][0]>l1[2][1]):
            pontos[0] = 3
            elif(l1[2][0] == l1[2][1]):
                pontos[0] = 1
                pontos[1] = 1
                else:
                    pontos[1] = 3
                    if(l2[0] == time1):
                        if(l2[2][0] > l2[2][1]):
                            pontos[0] = pontos[0] + 3
                            elif(l2[2][0] == l2[2][1]):
                                pontos[0] = pontos[0]+1
                                pontos[1] = pontos[1]+1
                                else:
                                    pontos[1] = pontos[1]+3
                                    if(l2[0] == time2):
                                        if(l2[2][0]>l2[2][1]):
                                            pontos[1] = pontos[1]+3
                                            elif(l2[2][0] == l2[2][1]):
                                                pontos[1] = pontos[1]+1
                                                pontos[0] = pontoss[0]+1
                                                else:
                                                    pontos[0] = pontos[0]+3
                                                    return {time1: pontos[0], time2: pontos[1]}