def num_bombons(din,preço):
	N = din//preço
	S = din - N*preço
	print("Número possível de bombons:", N)
	print("Dinheiro sobrando:", S)