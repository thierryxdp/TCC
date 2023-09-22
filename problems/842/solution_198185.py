def pontos_por_time(lista):
    lista1 = lista[0]
    lista2 = lista[1]
    timea1 = lista1[0]
    timea2 = lista1[1]
    timeb1 = lista2[0]
    timeb2 = lista2[1]
    time1 = 0
    time2 = 0
    placar= {}

    if ((lista1 [2][0]) > (lista1[2][1])):
        time1 = time1 + 3
    if ((lista1 [2][0]) < (lista1[2][1])):
        time2 = time2 + 3
    if ((lista1[2][0]) == (lista1[2][1])):
        time2 = time2 + 1
        time1 = time1 = +1
    if  ((lista2 [2][0]) > (lista2[2][1])):
        time2 = time2+ 3
    if  ((lista2 [2][0]) < (lista2[2][1])):
        time1 = time1+ 3
    if ((lista2[2][0]) == (lista2[2][1])):
        time2 = time2 + 1
        time1 = time1 +1
    if ((lista2[2][0]) < (lista2[2][1]) or (lista2[2][0]) == (lista2[2][1])):
        placar[timea1] = time1
        placar[timeb1] = time2
    if ((lista2[2][0]) > (lista2[2][1])):
        placar[timeb1] = time2
        placar[timea1] = time1

    return placar