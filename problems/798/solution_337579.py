def freq_palavras(frases):
    ''' '''
    palavra=frases.split()
    for nova in palavra:
        contagem= palavra.count(nova)
    	dicionario={}
		dicionario[nova]=contagem
    return dicionario