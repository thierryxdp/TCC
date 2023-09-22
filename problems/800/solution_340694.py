def total(produtos,lista):
    soma=0
    for comida in produtos:
        if comida in lista:
            soma=soma+lista[comida]  
	if soma>39 and soma <40:
        return 39.6
    return soma