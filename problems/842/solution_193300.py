def pontos_por_time(lista):
    '''oi
    tchau'''
    nome_t1 = lista[0][0]
    nome_t2= lista[1][0]
    pontostotal1 = 0
    pontostotal2 = 0
    if(lista[0][2][0] > lista[0][2][1]):
        pontostotal1 += 3
	elif(lista[0][2][0] < lista[0][2][1]):
        pontostotal2 += 3
	else:
        pontostotal1 += 1
        pontostotal2 += 1
	if(lista[1][2][1] > lista[1][2][0]):
       	pontostotal1 += 3
	elif(lista[1][2][1] < lista[1][2][0]):
        pontostotal2 +=3
	else:
        pontostotal1 +=1
        pontostotal2 +=1
    return {nome_t1:pontostotal1, nome_t2:pontostotal2}