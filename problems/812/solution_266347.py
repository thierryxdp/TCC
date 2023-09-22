#dado uma frase retorna a mesmo sem pontos
#str-->str
def retira_pontuacao(s):
	import string
	punct = string.punctuation
    for c in punct:
    	s = s.replace(c, "")
    return(s)