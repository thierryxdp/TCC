import re
def conta_frases(texto):
	print (re.split('[!.?]', texto))