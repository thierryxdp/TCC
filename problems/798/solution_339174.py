def freq_palavras(frases):
    '''Retorna um dicionário onde cada palavra da string inserida é uma
    chave e o número de vezes que ela aparece o valor correspondente;
    str -> dict'''
    dicionario={}
    frases=frases.split(' ')
    for i in range(len(frases)):
        dicionario[frases[i]]=frases.count(frases[i])
	return dicionario