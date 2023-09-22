def pontos_por_time(pontos):
    vit1A = pontos[0][2][0] > pontos[0][2][1]
    vit1B = pontos[0][2][1] > pontos[0][2][0]
    empate1 = pontos[0][2][0] == pontos[0][2][1]
    vit2A = pontos[1][2][0] > pontos[1][2][1]
    vitoria2B = pontos[1][2][1] > pontos[1][2][0]
    empate2 =  pontos[1][2][0] == pontos[1][2][1]
    pontA = 6
    pontB = 0
    resultado = {pontos[0][0]: pontA, pontos[0][1]: pontB}
    if vit1A and vit2A == True:
    pontA = 6
    pontB = 0
        return resultado