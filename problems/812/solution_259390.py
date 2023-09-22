def substitui(letra):

	pontos = ['.',',','!','?','-',':',';']

	if letra in pontos:
        return ' '

	else:
        return letra

def retira_pontuacao(letra):


	frase = ''.join(map(substitui,letra))

	return frase