def pontos_por_time(jogo_ida, jogo_volta):
    '''Função que aponta a quantidade pontos de um time e sua classificação'''

    vitoria = 3*1
    
    derrota = 0

    vitoria = [jogo_ida[2][0] > jogo_volta[2][0]]  
    empate = [jogo_ida[2][0] == jogo_volta[2][0]]
    derrota = [jogo_ida[2][0] < jogo_volta[2][0]]

      

    jogo_ida = [jogo_ida[0], jogo_ida[1],jogo_ida[2]]
    jogo_volta = [jogo_volta[0], jogo_volta[1], jogo_volta[2]]

    resultado_final = jogo_ida[0], jogo_volta[1], [jogo_ida[2][0] + jogo_volta[2][0]]  +  [jogo_ida[2][1] + jogo_volta[2][1]]
    if empate:
        return jogo_ida[0], jogo_volta[1], 2