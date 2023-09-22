def pontos_por_time(pontos):
    vit1A = pontos[0][2][0] > pontos[0][2][1]
    vit1B = pontos[0][2][1] > pontos[0][2][0]
    empate1 = pontos[0][2][0] == pontos[0][2][1]
    vitoria2A = pontos[1][2][0] > pontos[1][2][1]
    vitoria2B = pontos[1][2][1] > pontos[1][2][0]
    empate2 =  pontos[1][2][0] == pontos[1][2][1]
    pontosA = 0
    pontosB = 0
    resultado = {pontos[0][0]: pontosA, pontos[0][1]: pontosB}
    if vit1A and vit2A == True:
        pontosA = 6
        pontosB = 0
        return resultado