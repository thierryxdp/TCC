import re
def conta_frases(texto):
    texto = texto.replace("...",".")
	print (re.split('[!.?]*', texto))