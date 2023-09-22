def freq_palavras(frases):
    listaFrases = frases.split(" ")
    dicionarioF={}
    for i in range(len(listaFrases)):
        dicionarioF[i] = {listaFrases[i]:listaFrases.count(listaFrases[i])}
	return dicionarioF