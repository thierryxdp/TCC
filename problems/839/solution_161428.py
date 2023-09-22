from math import ceil
	def carros(pessoas,capacidade=5):
	#Função que calcula o número exato de carros necessários para que um grupo de amigos faça uma viagem, dados o número de pessoas e a capacidade dos veículos
	return ceil(pessoas/capacidade)