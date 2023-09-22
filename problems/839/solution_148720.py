def carros(x,y=5):
	carros = x//y
	resto = x % y
	if (resto > 0):
		return carros + 1
	elif (resto == 0):
		return carros