def media_matriz(matriz):
    soma = 0
    tamanho = 0
    for linha in matriz:
        for elemento in linha:
        	soma += sum(linha)
        	tamanho += len(linha)
   	return round((soma / tamanho),2)