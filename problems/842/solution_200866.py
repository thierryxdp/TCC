def pontos_por_time(jogos_e_resultado):
    ''' indica o resultado dos jogos e a quantiadade de pontos
    	de cada time na fase. list ---> list '''
    resultado1 = jogos_e_resultados[1]
    resultado2 = jogos_e_resultados[2]
    if resultado1[0] > resultado1[1] and resultado2[1] > resultado2[0]:
        return {jogos_e_resultados[0]: 6, jogos_e_resultados[1]: 0,}