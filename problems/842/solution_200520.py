def pontos_por_time(lista):
    timeA = lista[0][0]
    timeB = lista[0][1]
    golstimeAj1 = lista[0][2][0]
    golstimeAj2 = lista[1][2][1]
    golstimeBj1 = lista[0][2][1]
    golstimeBj2 = lista[1][2][0]
    pontosdotimeA = 0
    pontosdotimeB = 0
    if golstimeAj1 > golstimeBj1:
        pontosdotimeA += 3
    if golstimeBj1 > golstimeAj1:
        pontosdotimeB += 3
    if golstimeAj1 == golstimeBj1:
        pontosdotimeA += 1
        pontosdotimeB += 1
    if golstimeAj2 > golstimeBj2:
        pontosdotimeA += 3
    if golstimeBj2 > golstimeAj2:
        pontosdotimeB += 3
    if golstimeAj2 == golstimeBj2:
        pontosdotimeA += 1
        pontosdotimeB += 1
    return {timeA:pontosdotimeA, timeB:pontosdotimeB}