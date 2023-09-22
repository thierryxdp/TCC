import re
def conta_frases(texto):
	print (len(re.split("[!.?..] ", texto)))