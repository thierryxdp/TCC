def pontos_por_time([jogo_ida, jogo_volta]):
    '''retorna um dicionario com os nomes dos times e seus respectivos totais de pontos na fase, dados jogos de ida e volta'''
    '''list,list->dict'''
    t1=jogo_ida[0]
    t2=jogo_volta[0]
    pontos_t1=jogo_ida[2][0] + jogo_volta[2][1]
    pontos_t2=jogo_ida[2][1] + jogo_volta[2][0]
    
    return {t1:pontos_t1, t2:pontos_t2}