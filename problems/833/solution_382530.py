def conta_numero(numero, matriz):
    """Essa função, dado um número inteiro e uma matriz de inteiros,
	 conta e retorna quantas vezes o número aparece na matriz
     int, list -> int"""
    cont = 0
    for linha in matriz:
        for coluna in linha:
            if coluna == numero:
                cont += 1
    return cont