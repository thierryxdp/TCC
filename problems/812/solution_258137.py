def retira_pontuacao(frase):
    '''função que recebe uma string e retira todas suas pontuações, assim
    devolvendo outra string'''
    pontos = ['-',',',':',';','.','?','!','...']
	for i in range(len(pontos)):
		frase = frase.replace(pontos[i], ' ')
	return frase