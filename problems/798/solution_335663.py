def freq_palavras(frase):
    resp = {}
    frase = str.split (frase)
    for palavra in frase:
        resp[palavra] = resp.get(palavra,0) +1
	return resp