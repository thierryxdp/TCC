def freq_palavras(frases):
    frases=frases.slplit()
    lista = {}
    for palavra in frases:
        if palavra in lista:
            lista[palvra] +=1
        else:
            lista[palavra] = 1
	return lista