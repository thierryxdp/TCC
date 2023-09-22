def fatorial(numero):
    """Função que dado um numero calcula o fatorial dele.
    parametros:int->int"""
	resultado=1
	count=1

	while count <= numero:
    	resultado *= count
    	count += 1

	return (resultado)