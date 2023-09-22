def retira_pontuacao(frase):
	s = frase
	semponto = s.translate(str.maketrans('', '', string.punctuation))
	return semponto