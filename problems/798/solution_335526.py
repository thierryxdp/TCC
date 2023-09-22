def freq_palavras (frase):
    resposta = {}
    frase = str.split (frase)
    for palavra in frase:
        resposta[palavra] = resposta.get(palavra,0) +1
	return resposta