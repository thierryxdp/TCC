def conta_frases(txt):
	"""função que conta o número de frases que têm em um texto, segundo as pontuações ali presentes
str -> int"""
    a = str.count(txt,".") 
    b = str.count(txt,"...") 
	c = str.count(txt,"!") 
	d = str.count(txt,"?") 
    e = -3*b
	
    

	return a