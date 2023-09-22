def conta_frases(txt):
	"""função que conta o número de frases que têm em um texto, segundo as pontuações ali presentes
string -> string"""
    a = txt.count(".")
    b = txt.count("...")
	c = txt.count("!")
	d = txt.count("?")
	
    

	return a+b+c+d