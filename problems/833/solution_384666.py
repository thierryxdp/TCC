def conta_numero(numero, matriz):
    """Função que conta a quantidade de numeros do numero que foi 
    dado de entrada na matriz; int, list -> int """
    x = 0
    for i in matriz:
        for j in i:
            if numero == j:
                x += 1
	return x