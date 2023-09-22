def qtd_divisores(numero):
	"""Retorna o numero de divisores que um número tem.
    Parametros:
    Entrada:int
    Saida:int"""
    contador=0
	for indice in range(1,numero+1):
        if numero%indice==0:
        	contador=contador+1 
	return contador