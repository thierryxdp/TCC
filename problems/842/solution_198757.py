def pontos_por_time(jogo_ida, jogo_volta):
    '''Função que aponta a quantidade pontos de um time e sua classificação'''

    jogo_ida = [jogo_ida[0], jogo_ida[1],jogo_ida[2]]
    jogo_volta = [jogo_volta[0], jogo_volta[1], jogo_volta[2]]
    
    vitoria = jogo_ida[2][0] > jogo_volta[2][0]

    jogo_ida[2][0] > jogo_volta[2][0] == 3
    jogo_volta[2][0] > jogo_ida[2][0] == 3
    
    empate = jogo_ida[2][0] == jogo_volta[2][0]

    derrota_ida = jogo_ida[2][0] < jogo_volta[2][0]
    derrota_volta = jogo_volta[2][0] < jogo_ida[2][0] 

    if jogo_ida[2][0] > jogo_volta[2][0] and jogo_volta[2][1] > jogo_ida[2][1]:
         return {jogo_ida[0]:6, jogo_ida[1]:0}
    elif jogo_ida[2][0] < jogo_volta[2][0] and jogo_volta[2][1] < jogo_ida[2][1]:
         return {jogo_ida[0]:0, jogo_ida[1]:6}    
    elif jogo_ida[2][0] > jogo_volta[2][1] and jogo_ida[2][1] == jogo_volta[2][1]:
         return {jogo_ida[0]:4, jogo_ida[1]:1}
    elif jogo_ida[2][0] < jogo_volta[2][1] and jogo_ida[2][1] == jogo_volta[2][1]:
         return {jogo_ida[0]:1, jogo_ida[1]:4}
    elif jogo_ida[2][0] == jogo_volta[2][1] and jogo_ida[2][1] > jogo_volta[2][1]:
         return {jogo_ida[0]:4, jogo_ida[1]:1}
    elif jogo_ida[2][0] == jogo_volta[2][1] and jogo_ida[2][1] < jogo_volta[2][1]:
         return {jogo_ida[0]:1, jogo_ida[1]:4}

    else :
         return {jogo_ida[0]:2, jogo_ida[1]:2}