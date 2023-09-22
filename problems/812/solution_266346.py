#dado uma frase retorna a mesmo sem pontos
#str-->str
def retira_pontuacao(a):
	import string 
	x="!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
	for y in x:
		a=a.replace(x,"")
	return a