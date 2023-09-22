import re
def conta_frases(texto):
    texto = texto.replace("...",".")
	len(re.split("[!.?] ", texto))