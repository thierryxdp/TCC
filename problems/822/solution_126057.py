def repetidos(lista):
    contador = 1
    ocorrencia = 0
    while contador<len(lista):
        if lista[contador] == lista[contador-1]:
            ocorrencia = ocorrencia + 1
	return ocorrencia