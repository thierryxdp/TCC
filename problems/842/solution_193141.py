def pontos_por_time(lista):
    cpontos=0
    fpontos=0
	#cormengo
    if lista[0][2][0]>lista[0][2][1]:
        cpontos+=3
        
    elif lista[0][2][0]=ista[0][2][1]:
        cpontos+=1
        fpontos+=1
    else:
        fpontos+=3
    
    if lista[1][2][1]>lista[1][2][0]:
		cpontos+=3
    elif lista[1][2][1]=lsta[1][2][0]:
        cpontos+=1
        fpontos+=1
    else:
        fpontos+=3
        
	dicionario={lista[0][0:cpontos,lista[0][1]:fpontos}
    return dicionario