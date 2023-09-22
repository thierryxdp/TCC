def freq_palavras(frases):
    ''' '''
    dicionario={}
    palavra=frases.split()
    for nova in palavra:
        contagem= palavra.count(nova)
		dicionario[nova]=contagem
    return dicionario