def conta_frases(frase):
'''Esta funçao retorna a quantidade de frases que aparecem no texto
string ===> int'''
	frase = frase.replace('.' , '$')
   	frase = frase.replace('!' , '$')
    frase = frase.replace('...' , '$)
                  
	return frase.count('$')