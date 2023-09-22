def lingua_p(palavra):
    """..."""
    string_palavra = ""
    contador = 0
    while contador <= len(palavra):
        if palavra[contador] in "AEIOUaeiou":
            string_palavra = string_palavra + palavra[contador] + "p"
		else:
            string_palavra = string_palavra + palavra[contador]
		contador = contador + 1
	return string_palavra