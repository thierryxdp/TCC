def inverte(texto: str):

	lista = texto.split(" ")
	lista.inverte()


	new_text = " ".join(lista)

	return new_text.lower()