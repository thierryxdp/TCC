def retira_pontuacao(frase):
	""" Esta função tira a pontuação das frases
	str -> str"""
	
	#trocar pontuacao
	frase = frase.replace('...','')
	#trocar pontuacao
    frase = frase.replace('-',' ')
    #trocar pontuacao
    frase = frase.replace(':','')
    #trocar pontuacao
    frase = frase.replace(',','')
    #trocar pontuacao
    frase = frase.replace('.','')
    #trocar pontuacao
    frase = frase.replace('?','')
    #trocar pontuacao
    frase = frase.replace('!','')

	return frase


def inverte(frase):
	""" Esta função inverte a frase
	str -> str """
	#trocar pontuacao
	x = retira_pontuacao(frase)
	
	#divide em lista e inverte a posição
	y = str.split(str.strip(x,' '),' ')
	list.reverse(y)
	z = str.join (' ',y)
	#retorna em letras minusculas
	return str.lower(z)