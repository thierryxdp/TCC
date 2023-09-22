def substitui(letra):

	pontos = ['.',',','!','?','-',':',';']

	if pontos in letra:
        return ' '

	else:
        return letra

def retira_pontuacao(letra):


	frase = ''.join(map(substitui,letra))

	return frase