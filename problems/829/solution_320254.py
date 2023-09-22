def soma_h(n):
    """Função que dado como entrada o número inteiro n, calcula e retorna a soma
    dos termos até o valor n.
    int -> float.
    """
    soma = 0
    x = list(range(1,n+1))
    for numero in x:
	    if n == int(n):
		    calculo = (1/numero)
		    soma += calculo
    return round(soma,2)