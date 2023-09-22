def lingua_p(palavra):
    """..."""
    string_palavra = ""
    for contador in range(len(palavra)):
        if palavra[contador] in "AEIOUaeiouáÁúÚéÉ":
            string_palavra = string_palavra + palavra[contador] + "p" + palavra[contador]
		else:
            string_palavra = string_palavra + palavra[contador]
	return string_palavra