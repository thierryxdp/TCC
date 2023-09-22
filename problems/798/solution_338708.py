def freq_palavras(frases):
    """A função conta a frequencia de uma palavra e retorna um dicionario com a quantidade de frequecia
    Str --> disc """
    r = str.split(frases, " ")
    D = {}
	for x in r:
        if x in r:
            D[x] = list.count(r, str(x))
	return D