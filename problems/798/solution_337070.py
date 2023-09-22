def freq_palavras(frases):
	"""Recebe uma string e retorna um dicionário no qual acada plavra dessa string é uma chave o o valor corresponde ao número de vezes que a palavras aparece na string ; str->dict."""
    frases=retira_pontuacao(frases)
	lista_frases=str.split(frases," ")
    dic_freq={}
    for palavras in lista_frases:
        freq=list.count(lista_frases,palavras)
        dic_freq[palavras]=freq
	return dic_freq