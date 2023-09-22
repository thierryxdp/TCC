def retira_pontuacao(frase):
    x = list(frase)
	retira_pont:map(lambda x: x = ' 'if x == '.')
    s =' '.join(x)
    return s