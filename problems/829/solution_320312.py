def soma_h(N:int) -> float:
    """Função que irá somar elementos como: 1 + 1/2 + 1/3 + 1/4 + ... + 1/N. Essa sequência se inicia no número 1 e termina em 1/N, possuindo ao todo N termos.
    int -> float

        Parameters:
        N: número inteiro

        Returns:
        soma da sequência explicada acima
    """
    soma_h = 0
	for numero in range(1, N):
        soma_h = soma_h + range((1/numero), 2)
    return round(soma_h, 2)