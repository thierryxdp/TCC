def pontos_por_time(lista1,lista2):
    timea1 = lista1[0]
    timea2 = lista1[1]
    timeb1 = lista2[0]
    timeb2 = lista2[1]
    

    if ((lista1 [2][0]) > (lista1[2][1])):
        placar =
    if ((lista1 [2][0]) < (lista1[2][1])):
        placar[timeb] = +3
    if ((lista1[2][0]) == (lista1[2][1])):
        placar[timea] = +1
        placar[timeb] = +1
    if  ((lista2 [2][0]) > (lista2[2][1])):
        placar[timeb] = +3
    if  ((lista2 [2][0]) < (lista2[2][1])):
        placar[timea] = +3
    if ((lista2[2][0]) == (lista2[2][1])):
        placar[timea] = +1
        placar[timeb] = +1
   
	return placar