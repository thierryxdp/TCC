def faltante(lista):
    lista.sort()
    numerofinal = 0
    for num in lista:
        numerofinal = num
    for num in range(1,numerofinal):
        if num != lista[num-1]:
            return num
	return numerofinal + 1