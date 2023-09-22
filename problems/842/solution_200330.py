pontos_por_time (nome1,nome2,pontos_f,pontos_c):
    '''funcao que retorna o nome do time e numero de pontos'''
    cont_c = 0
pontos_f = 0
pontos_c += pontos[0] * 3 
pontos_c += pontos[1] * 1
pontos_f += pontos[3] * 3
pontos_f += pontos[4] * 1
if pontos_c > pontos_f:
    return("C")
elif pontos_c < pontos_f:
    return("F")
else:
    if pontos[2] > pontos[5]:
        return("C")
    elif time[2] == time[5]:
        return("=")
    else:
        return("F")