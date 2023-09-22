def pontos_por_time(lista):
    pontosA=[]
    pontosB=[]
    if lista[0][2][0]>lista[0][2][1]:
        pontosA+=3
	elif lista[0][2][0]==lista[0][2][1]:
        pontosA+=1
        pontosB+=1
    else:
        pontosB+=3
	if lista[1][2][0]>lista[1][2][1]:
        pontosB+=3
	if lista[1][2][0]==lista[1][2][1]:
        pontosB+=1
        pontosA+=1
	else:
        pontosA+=3
	dicionario{lista[0][1][1]:pontosA,lista[0][1][2]}
    return dicionario