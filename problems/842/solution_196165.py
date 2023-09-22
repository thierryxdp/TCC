def pontos_por_time(jogo_ida,jogo_volta):   
    nome_time1 = jogo_ida [0]
    nome_time2 = jogo_volta[0]
    num_pontos1 = jogo_ida[2][0]+ jogo_volta[2][1]
    num_pontos2 = jogo_ida[2][1]+ jogo_volta[2][0]
    return {nome_time1:num_pontos1, nome_time2:num_pontos2}