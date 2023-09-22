def bolos(A,B,C):
	farinha=A
	ovos=B
	colheres=C
	ingredientes=[farinha,ovos,colheres]
	list.sort(ingredientes)

    if ingredientes[0] == farinha:
    	return farinha//2
	elif ingredientes[0] == ovos:
    	return ovos//3
	else:
    	return colheres//5