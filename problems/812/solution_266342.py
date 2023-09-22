#dado uma frase retorna a mesmo sem pontos
#str-->str
def retira_pontuacao(a):
	x=string.punctuation
	for y in x:
		a=a.replace(x,'')
	return a