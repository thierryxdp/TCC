#dado uma frase retorna a mesmo sem pontos
#str-->str
def retira_pontuacao(a):
	import string
	z = string.punctuation
    for x in z:
    	a = a.replace(x, )
    return(a)