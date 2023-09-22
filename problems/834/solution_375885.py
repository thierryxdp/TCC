def media_matriz(m):
    soma = 0
    tamanho = 0
    for linha in m:
        soma += sum(linha)
    	tamanho += len(linha)
    return soma / tamanho