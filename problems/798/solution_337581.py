def freq_palavras(frases):
    '''Função que pega a frase de entrada, identifica cada palavra e retorna em um dicionário quantas vezes ela aparece
    str, str→dict'''
    dicionario={}
    palavra=frases.split()
    for nova in palavra:
        contagem= palavra.count(nova)
		dicionario[nova]=contagem
    return dicionario