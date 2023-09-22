def conta_numero(numero:int, matriz:list[list])->int:
    contador = 0
    for i in matriz:
        for j in i:
            if j == numero:
                contador += 1
	return contador