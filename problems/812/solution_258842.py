def retira_pontuacao(frase):
	''' '''
	filtro = str.replace(frase,'.',' ')
	filtro1 = str.replace(filtro,'-',' ')
    filtro2 = str.replace(filtro1,',',' ')
    filtro3 = str.replace(filtro2,';',' ')
	filtro3 = str.replace(filtro2,';',' ')
	filtro4 = str.replace(filtro3,'?',' ')
	filtro5 = str.replace(filtro4,'!',' ')

	return filtro5