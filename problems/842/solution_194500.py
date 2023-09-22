def pontos_por_time(lista):
    """"Calcula a pontuação de dois times e retorna um dicionário cujos
    mapeamentos são: <nome do time> → <numero de pontos na fase>;
    list -> dict"""
    time1_lista1 = lista[0][0]
    time2_lista1 = lista[0][1]
    time1_lista2 = lista[1][0]
    time2_lista2 = lista[1][1]

    gols_time1_lista1 = lista[0][2][0]
    gols_time2_lista1 = lista[0][2][1]
    gols_time1_lista2 = lista[1][2][0]
    gols_time2_lista2 = lista[1][2][1]

    time1_iguais = (time1_lista1 == time1_lista2)

    vitoria_time1_jogo1 = (gols_time1_lista1 > gols_time2_lista1)
    vitoria_time1_jogo2 = (gols_time1_lista2 > gols_time2_lista2)
    
    empate_jogo1 = (gols_time1_lista1 == gols_time2_lista1)
    empate_jogo2 = (gols_time1_lista2 == gols_time2_lista2)
    
    if time1_iguais:
        if vitoria_time1_jogo1:
            pontuacao_time1_jogo1 = 3
            pontuacao_time2_jogo1 = 0
        elif empate_jogo1:
            pontuacao_time1_jogo1 = 1
            pontuacao_time2_jogo1 = 1
        else:
            pontuacao_time1_jogo1 = 0
            pontuacao_time2_jogo1 = 3
        if vitoria_time1_jogo2:
            pontuacao_time1_jogo2 = 3
            pontuacao_time2_jogo1 = 0
        elif empate_jogo2:
            pontuacao_time1_jogo2 = 1
            pontuacao_time2_jogo1 = 1
        else:
            pontuacao_time1_jogo2 = 0
            pontuacao_time2_jogo1 = 3
        pontuacao_total_time1 = pontuacao_time1_jogo1 + pontuacao_time1_jogo2
        pontuacao_total_time2 = pontuacao_time2_jogo1 + pontuacao_time2_jogo2
        dicionario_pontuacoes = {time1_lista1 : pontuacao_total_time1, time2_lista1 : pontuacao_total_time2}
        return dicionario_pontuacoes
    else:
        if vitoria_time1_jogo1:
            pontuacao_time1_jogo1 = 3
            pontuacao_time2_jogo1 = 0
        elif empate_jogo1:
            pontuacao_time1_jogo1 = 1
            pontuacao_time2_jogo1 = 1
        else:
            pontuacao_time1_jogo1 = 0
            pontuacao_time2_jogo1 = 3
        if vitoria_time1_jogo2:
            pontuacao_time1_jogo2 = 3
            pontuacao_time2_jogo2 = 0
        elif empate_jogo2:
            pontuacao_time1_jogo2 = 1
            pontuacao_time2_jogo2 = 1
        else:
            pontuacao_time1_jogo2 = 0
            pontuacao_time2_jogo2 = 3
        pontuacao_total_time1 = pontuacao_time1_jogo1 + pontuacao_time2_jogo2
        pontuacao_total_time2 = pontuacao_time2_jogo1 + pontuacao_time1_jogo2
        dicionario_pontuacoes = {time1_lista1 : pontuacao_total_time1, time2_lista1 : pontuacao_total_time2}
        return dicionario_pontuacoes