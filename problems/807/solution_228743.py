import re
def conta_frases(texto):
    texto = texto.replace("...",".")
	print (len(re.split(r'[!.?]+', texto)))