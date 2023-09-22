def busca(setor, dados):
	dadosEncontrados = list(filter(lambda dado: verificaSetor(setor, dado), dados))

	resultado = list(map(coletaDados, dadosEncontrados))
	return resultado

def verificaSetor(setor, dados):
	return dados[2] == setor

def coletaDados(dado):
	dadoCopy = dado.copy()
	dadoCopy.pop(-2)
	return dadoCopy