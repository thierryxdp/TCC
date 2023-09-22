#Start your python function here
def pontos_por_time(lista):
    jogo1_1 = [0][2][0]
    jogo1_2 = [0][2][1]
    jogo2_1 = [1][2][0]
    jogo2_2 = [1][2][1]
    
    if jogo1_1 > jogo1_2:
        jogo1_1 == 3 and jogo1_2 == 0
    if jogo1_1 < jogo1_2:
        jogo1_1 == 0 and jogo1_2 == 3
    if jogo2_1 > jogo2_2:
        jogo2_1 == 3 and jogo2_2 == 0
    if jogo2_1 < jogo2_2:
        jogo2_1 == 0 and jogo2_2 == 3
        
    pontoA = jogo1_1 + jogo2_2
    pontoB = jogo1_2 + jogo2_1
    
    return {[0][0]:pontoA,[0][1]:pontoB}