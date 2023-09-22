def lingua_p(palavra):
	#Variaveis para armazenar a palavra traduzida e o conjunto das vogais em forma de lista
	nova_palavra = ""
	vogais = ["a","e","i","o","u","á","ã","à","a","â","é","ê","í","õ","ô","ú"]
	"""Percorrendo a palavra original de modo que posso montar a palavra traduzida com base nela.
	Confiro se a letra é vogal, caso seja, aplico a regra, caso não seja, apenas adiciono normalmente"""
	for letra in palavra.lower():
		if letra in vogais:
			nova_palavra += letra + "p" + letra
		else:
			nova_palavra += letra
	return nova_palavra