def freq_palavras(frase):
	'''Esta função recebe frase e retorna um dicionário com
	a quantidade de cada palavra da string
	str--> dict'''
	palavras = frase.split()
	dict1 = {}
	counter = 0
    
	for elementos in palavras:
		dict1[palavras[counter]] = palavras.count(palavras[counter])
		counter += 1
	return dict1