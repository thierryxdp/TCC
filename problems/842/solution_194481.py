def pontos_por_time(jogo_ida, jogo_volta):
    '''retorna um dicionario com os nomes dos times e seus respectivos totais de pontos na fase, dados jogos de ida e volta'''
    '''list,list->dict'''
    
    time1='jogo_ida[0]'
    time2='jogo_volta[0]'
    pontos1=jogo_ida[2][0] + jogo_volta[2][1]
    pontos2=jogo_ida[2][1] + jogo_volta[2][0]
    info1='time1:pontos1'
    info2='time2:pontos2'
    
    return {info1, info2}