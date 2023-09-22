def pontos_por_time(lista):
    primeiro=lista[0][0]
    segundo=lista[0][1]
    cpontos=0
    fpontos=0
    
    if lista[0][2][0]>lista[0][2][1]:
        cpontos+=3
    elif lista[0][2][0]==lista[0][2][1]:
        cpontos+=1
        fpontos+=1
    else:
        fpontos+=3
        
        
	if lista[1][2][1]>lista[1][2][0]:
        cpontos+=3
    elif lista[1][2][1]==lista[1][2][0]:
        cpontos+=1
        fpontos+=1
    else:
        fpontos+=3
        
    dicionario={primeiro:cpontos,segundo:fpontos}7
    return dicionario