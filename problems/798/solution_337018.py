def freq_palavras(frases):
    """reecebe uma string e retorna um dicionário no qual acada plavra dessa string é uma chave o o valor corresponde ao número de vezes que a palavras aparece na string ; str->dict."""
    palavras=str.split(frases)
    i=0
    dic_freq={}
    for palavras[i] in palavras:
		freq=list.count(palavras,palavras[i])
		dic_freq={palavras[i]:freq}
        i+=1
    return dic_freq