def inverte(frase):
  	'''inverte a ordem das palavras de uma frase qualquer
    str -> str'''
  	palavras = subs_por_espaco(frase).lower().split()
  	frase_invertida = ' '.join(palavras[::-1])
  	return frase_invertida