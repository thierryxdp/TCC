def pontos_por_time(resultado1, resultado2):

    

    

    pontos = {}
    
    pontos[resultado1[0][0][0]] = 0

    pontos[resultado1[0][0][1]] = 0

    if resultado1[0][2][0] > resultado1[0][2][1]:

        pontos[resultado1[0][0]] = pontos[resultado1[0][0]] + 3

    elif resultado1[0][2][0] < resultado1[0][2][1]:

        pontos[resultado1[0][1]] = pontos[resultado1[0][1]] + 3
    
    elif resultado1[0][2][0] == resultado1[0][2][1]:

        pontos[resultados1[0][0]] = pontos[resultado1[0][0]] + 1

        pontos[resultado1[0][1]] = pontos[resultado1[0][1]] + 1