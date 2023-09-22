def retira_pontuacao(x):
  	for character in x.punctuation:
    x = x.replace(character, '')
	return x