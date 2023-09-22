# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
freq_palavras(frases):
    dicionario = {}
    palavras = frases.split(" ")
    for palavra in palavras:
        if palavra in list(dicionario.keys()):
            dicionario[palavra] += 1
		else:
            dicionario[palavra] = 1
	return dicionario