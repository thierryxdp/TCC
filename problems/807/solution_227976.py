def conta_frases(frase):
'''Esta funçao retorna a quantidade de frases que aparecem no texto
string ===> int'''
    frase.replace('.' , '$')
    frase.replace('!' , '$')
    frase.replace('...' , '$)
	return frase.count('$')