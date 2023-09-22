def media(matriz):
    "Função que recebe uma matriz e retorna a média de seus números."
    "list -> list"
	soma = 0
	tamanho = 0
	for linha in matriz:
    	soma += sum(linha)
    	tamanho += len(linha)
  	return soma / tamanho