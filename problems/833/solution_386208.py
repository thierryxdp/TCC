def conta_numero(numero,matriz):
    """
    	Função que conta quantas vezes o número dado aparece
        na matriz.
    	int, list(list) -> int
    """
    repeticoes = 0
    for linhas in matriz:
        for elemento in linhas:
            if elemento == numero:
                repeticoes += 1
    return repeticoes