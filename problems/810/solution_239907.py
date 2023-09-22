def retira_pontuacao(frase):
	''' '''
	filtro = str.replace(frase,'.',' ')
	filtro1 = str.replace(filtro,'-',' ')
    filtro2 = str.replace(filtro1,',',' ')
    filtro3 = str.replace(filtro2,';',' ')
	filtro3 = str.replace(filtro2,';',' ')
	filtro4 = str.replace(filtro3,'?',' ')
	filtro5 = str.replace(filtro4,'!',' ')
	
	minuscula = str.lower(filtro5)
	lista_palavra = str.split(minuscula)
	lista_inversa = lista_palavra[::-1]
	return str.join(' ',lista_inversa)