def retira_pontuacao(x):
  	new_string = x.translate({ord('a'):None})
	return(new_string)