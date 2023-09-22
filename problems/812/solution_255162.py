def retira_pontuacao(x):
	z = [".",",",";",":","/"]
	for i in z:
		str.replace(x,i," ")
		x = x
	return x