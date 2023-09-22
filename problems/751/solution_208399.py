def quant_palavras(s):
	""" A função conta quantas letras há em uma frase;
    str -> int """
    phrase = str.split(s)
    letters = len(phrase)
    return letters