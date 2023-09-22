def inverte(texto: str):

	lista = texto.split(" ")
	
    lista.reverse()


	new_text = " ".join(lista)

	return new_text.lower()