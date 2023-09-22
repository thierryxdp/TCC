def freq_palavras(frase):
    resp = {}
    frase = str.split (frase)
    for palavra in frase:
        resp[palavra] = respo.get(palavra,0) +1
	return resposta