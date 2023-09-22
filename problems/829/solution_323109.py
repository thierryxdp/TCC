def soma_h(numero):
    """Dado um número, a função irá fazer a soma
    da divisão de 1 por todos os números que vão de 1
    até o número dado.
    Tipo da variável numero: int
    Tipo da saída: float"""
    H = 0
    for contador in range(1,numero+1):
		H = H + 1/contador
	return round(H, 2)