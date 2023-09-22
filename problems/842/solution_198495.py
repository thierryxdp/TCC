#Start your python function here
def pontos_por_time(lista):
    pontos = dict()
    for elemento of lista:
        if elemento[2][0] > elemento[2][1]:
            if elemento[0] not in pontos.keys():
                pontos[elemento[0]] = 0
            pontos[elemento[0]] += 3
        elif elemento[2][0] < elemento[2][1]:
            if elemento[1] not in pontos.keys():
                pontos[elemento[1]] = 0
            pontos[elemento[1]] += 3
        else:
            if elemento[0] not in pontos.keys():
                pontos[elemento[0]] = 0
            pontos[elemento[0]] += 1
            
            if elemento[1] not in pontos.keys():
                pontos[elemento[1]] = 0
            pontos[elemento[1]] += 1
    return pontos