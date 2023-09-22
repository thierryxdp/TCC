def conta_frases(frase):
	 punct = string.punctuation
	 for c in punct:
	 frase = str(frase.replace(c," "))
	 return len(frase.split('.'))+len;9split('?')+len(frase.split('!'))