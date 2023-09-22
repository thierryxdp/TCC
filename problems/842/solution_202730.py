def pontos_por_time(lista_recebida):
    """A função compara os valores dos placares dos jogos, definindo se houve uma vitória, um empate ou uma derrota para cada time e computa a pontuação de acordo com os respectivos resultados, definindo a pontuação de cada time"
    assinatura: int, int -> dict"""
    time1 = lista_recebida[0][0]
    time2 = lista_recebida[0][1]
    pontos1 = 0
    pontos2 = 0
    
    for jogo in lista_recebida:
        if jogo[2][0] > jogo[2][1]:
            if jogo[0] == time1:
                pontos1 += 3
            else:
                pontos2 += 3
        elif jogo[2][0] < jogo[2][1]:
            if jogo [0] == time1:
                pontos2 += 3
            else:
                pontos1 += 3
        else:
            pontos1 += 1
            pontos2 += 1
    tabela_de_pontos = [(time1, pontos1), (time2, pontos2)]
    pontos_time = dict(tabela_de_pontos)
    return pontos_time