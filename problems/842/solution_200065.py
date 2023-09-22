def pontos_por_time(pontos):
    vitoria1A = pontos[0][2][0] > pontos[0][2][1]
    vitoria1B = pontos[0][2][1] > pontos[0][2][0]
    empate1 = pontos[0][2][0] == pontos[0][2][1]
    vitoria2A = pontos[1][2][0] > pontos[1][2][1]
    vitoria2B = pontos[1][2][1] > pontos[1][2][0]
    empate2 =  pontos[1][2][0] == pontos[1][2][1]
    resultado = {pontos[0][0]:pontosA, pontos[0][1]:pontosB}
    if vitoria1A and vitoria2A == True:
        pontosA = 6
        pontosB = 0
        return resultado