def pontos_por_time ([[jogo1,],[jogo2,]]):
    if jogo1[2] > jogo1[3]:
        x = 3
        w = 0
    if jogo1[2] > jogo1[3]:
        x = 1
        w = 1
    if jogo1[2] < jogo1[3]:
        x = 0
        w = 3
    if jogo2[2] < jogo2[3]:
        y = 3
        z = 0
    if jogo2[2] < jogo2[3]:
        y = 1
        z = 1
    if jogo2[2] > jogo2[3]:
        y = 0
        z = 3
    tabela = {jogo1[0]:x+y, jogo1[1]:w+z}
    return
        tabela