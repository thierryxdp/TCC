def quant_palavras(frase):
	"""função que recebe uma string e retorna o número de 
    palavras da frase na string
    str -> <quantidade>"""
    frase = str.split(str.strip(frase))
    quantidade =len(frase)
    return quantidade