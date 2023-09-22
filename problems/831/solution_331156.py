def lingua_p(palavra):
    """..."""
    string_palavra = ""
    for contador in len(palavra):
        if palavra[contador] in "AEIOUaeiou":
            string_palavra = string_palavra + palavra[contador] + "p"
		else:
            string_palavra = string_palavra + palavra[contador]
	return string_palavra