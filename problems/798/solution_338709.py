def freq_palavras(frases):
    """A função conta a frequencia de uma palavra e retorna um dicionario com a quantidade de vezes que ela se repete
    Str --> disc """
    r = str.split(frases, " ")
    D = {}
	for x in r:
        if x in r:
            D[x] = list.count(r, str(x))
	return D