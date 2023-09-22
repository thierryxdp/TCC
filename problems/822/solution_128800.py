#dado uma lista de número inteiros retonra o números de vezes que o elemento da lista é igual ao elemento anterior
#list-->int
def repetidos(ls):
	x=0
	ft=ls[1:len(ls)-10]
	for i in range(len(ft)):
		if ls[i]==ls[i]:
			x=x+1
	return x