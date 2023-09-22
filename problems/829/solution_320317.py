def soma_h(N:int) -> float:
    """Função que irá somar elementos como: 1 + 1/2 + 1/3 + 1/4 + ... + 1/N. Essa sequência se inicia no número 1 e termina em 1/N, possuindo ao todo N termos.
    int -> float

        Parameters:
        N: número inteiro

        Returns:
        soma da sequência explicada acima
    """
    soma_h = 0
	for numero in range(1, N+1):
        soma_h = soma_h + (1/numero)
    return round(soma_h, 2)