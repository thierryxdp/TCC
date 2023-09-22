def retira_pontuacao(frase):
    """Recebe uma frase e a retorna sem pontuacao; str-> str."""
    frase= frase.replace("."," ")
    frase=frase.replace(","," ")
    frase=frase.replace(":"," ")
    frase=frase.replace("-"," ")
    frase=frase.replace(";"," ")
    frase=frase.replace("!"," ")
    frase=frase.replace("?"," ")
    return frase
def freq_palavras(frases):
	"""Recebe uma string e retorna um dicionário no qual acada plavra dessa string é uma chave o o valor corresponde ao número de vezes que a palavras aparece na string ; str->dict."""
    frases=retira_pontuacao(frases)
	lista_frases=str.split(frases," ")
    palavras=lista_frases[i]
    dic_freq={}
    for palavras in lista_frases:
        freq=list.count(lista_frases,palavras)
        dic_freq[palavras]=freq
	return dic_freq