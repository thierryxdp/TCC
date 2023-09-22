def conta_frases(frases):
    """Calcula e retorna a o número de frases que tem na
variável de entrada frases; str --> int"""
    y= frases.count("!")+ frases.count("?")+ frases.count("...")+frases.count(".")
    if ("..." and ".") in frases: 
    	return (y - ((frases.count("..."))*3))
	else:
        return y