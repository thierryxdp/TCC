def soma_h(inteiro):
    numeros = list(range(inteiro))
	list.append(numeros,inteiro)
    H = 0
    for numero in numeros:
        if numero > 0:
        	H += 1/numero
    return round(H,2)