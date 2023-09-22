import math
def carros(qntd_pessoas, cap=5):
    '''Função que retornará a quantidade de carros necessarios para transportar uma certa quantidade de pessoas, caso não seja dado nenhum valor para a capacidade do veiculo, o valor default sera 5. int, int -> int'''
	return math.ceil(qntd__pessoas/cap)