def pontos_por_time(lista1,lista2):
    timea = lista1[0]
    timeb = lista2[0]
    placar = {timea : 0, timeb: 0}

    if ((lista1 [2][0]) > (lista1[2][1])):
        placar[timea] = +3
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
	return lista2