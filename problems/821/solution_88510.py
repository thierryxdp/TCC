def fatorial(numero):
    """Função que dado um numero calcula o fatorial dele.
    parametros:int->int"""
	r_fatorial = 1
	i = 1

	while i <= numero:
    	r_fatorial *= i
    	i += 1

	return (r_fatorial)