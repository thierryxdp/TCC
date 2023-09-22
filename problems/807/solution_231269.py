def conta_frases(frases):
    """Retornar uma função que conte o n° de frases que aparecem em um determiando texto, sendo usado os diferentes tipos de pontuação para numerar uma frase; str=>sint"""
interrogacao = str.count(frases,"?")
exclamacao = str.count(frases,"!")
reticencias = str.count(frases,"...")
ponto = str.count(frases,".")
	return interrogacao + exclamacao + reticencias + ponto