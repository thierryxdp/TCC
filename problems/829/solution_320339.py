def soma_h(n):
    """Retorna o resultado de H com duas casa decimais.
    Parametros:
    Entrada:Float
    Saida:Float"""
    soma=0
	for indice in range(1,n+1):
		soma=soma+1/indice
    return round(soma,2)