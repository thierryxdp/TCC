import math
	def carros(npessoas,cap=5):
  	"""função que descreve o número de carros necessário para transportar um número n de pessoas, caso a capacidade do carro não seja informada, um valor default da capacidade será usado como 5"""
  	return round(npessoas/cap)