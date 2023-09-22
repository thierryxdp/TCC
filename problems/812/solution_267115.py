def retira_pontuacao(x):
  	new_string = x.translate({ord('.'):None})
print(new_string)