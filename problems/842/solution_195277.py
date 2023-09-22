def pontos_por_time(lista):
    dicio = {lista[0][0]:0, lista[0][1]:0}
    gols1 = lista[0][2]
    if gols1[0] < gols1[1]:
        dicio[lista[0][1]] += 3
    elif gols1[0] > gols1[1]:
        dicio[lista[0][0]] += 3
    else:
        dicio[lista[0][0]] += 1
        dicio[lista[0][1]] += 1
        
    gols2 = lista[1][2]
    
    if gols2[0] < gols2[1]:
        dicio[lista[0][0]] += 3
    elif gols2[0] > gols2[1]:
        dicio[lista[0][1]] += 3
    else:
        dicio[lista[0][0]] += 1
        dicio[lista[0][1]] += 1

    return dicio