def freq_palavras(frases):
    '''recebe uma frase e conta quantas vezes derteminada palavras aparece naquela frase
    str->list'''
    vezes_que_apareceu = {}
    palavras= []
    for i in frases:
        if i not in palavras:
            list.append(palavras,i)
            vezes_que_apareceu[i] = frases.count(i)
	return vezes_que_apareceu