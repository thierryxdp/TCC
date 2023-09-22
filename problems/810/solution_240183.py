def reverso(texto: str):

	lista = texto.split(" ")
	lista.reverse()


	new_text = " ".join(lista)

	return new_text.lower()


teste = reverso('Nossa, como eu gosto de chocolate.')

print(teste)