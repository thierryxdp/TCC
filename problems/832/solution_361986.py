def eh_quadrada(matriz):
    linha = len(matriz)
    for i in matriz:
        if len(i) != linha:
            return False
	return True