def fatorial(numero):
    """Calcula a fatorial de um número, ou seja, a multiplicação de todos os números
    anteriores a ele incluindo ele próprio.
    Tipo da variável numero: int
    tipo da saída: int"""
    index = 1
    resultado = 1
    while index <= numero:
        resultado = resultado * index
        index = index + 1
	return resultado