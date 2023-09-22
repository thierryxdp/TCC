def retira_pontuacao(frase):
	''' '''
	filtro = str.replace(frase,'.',' ')
	filtro1 = str.replace(filtro,'-',' ')
    filtro2 = str.replace(filtro1,',',' ')
    filtro3 = str.replace(filtro2,';',' ')
	
	return filtro3