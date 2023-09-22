def freq_palavras (frase):
    resposta = {}
    frase = str.split (frase)
    for palavra in frase:
        qtd = str.count(frase,palavra)
        resposta[palavra] = qtd
	return resposta