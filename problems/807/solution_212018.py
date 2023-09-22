"""Recebe uma string e retorna a quantidade de frases nela, baseada 
nas pontuações"""
"""str->int"""
def conta_frases(string):
	pt_final = string.count(".")
    if "..." in string:
        pt_final = pt_final - string.count("...")
	exclamacao = string.count("!")
	interrogacao = string.count("?")
	return pt_final + exclamacao + interrogacao