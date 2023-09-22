def carros(passageiros,capacidade=5):
	'int,int -> int ; Função para calcular o número de carros para transportar a quantidade de passageiros respeitando a capacidade do carro'
	'Necessidade de importar do módulo math a função ceil para arrendondar os valores para cima'
    import math
    return math.ceil(passageiros/capacidade)