def conta_frases(txt):
	"""função que conta o número de frases que têm em um texto, segundo as pontuações ali presentes
string -> string"""
    a = txt.count(".")
    b = txt.count("...")
	c = txt.count("!")
	d = c-(3*b)
	e = txt.count("?")
    

	return a+b+c+d+e