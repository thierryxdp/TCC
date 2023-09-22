def primo(numero):
    """Dado um número, a função irá checar se ele é primo ou não,
    ou seja, se só possui dois divisores, o 1 e o próprio número.
    Caso ele seja primo, o retorno será True, caso não seja,
    o retorno será False.
    Tipo da variável numero: int
    Tipo da saída: boolean"""
    divisores = 0
    for contador in range(1,numero+1):
        if numero%contador == 0:
            divisores = divisores + 1
	return divisores == 2