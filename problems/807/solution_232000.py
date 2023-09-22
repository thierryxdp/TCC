#Dado um texto retorna o número de frases
#str-->int
def conta_frases(a)
	x=a.count(".")
	y=a.count("!")
	z=a.count("?")
	b=a.count("...")
	return x+y+z+b