def media_matriz(matriz):
    '''
		Função que retorna seu resultado com somente duas casa decimais.
		List => Float
    '''
    quantidade = 0
    soma = 0
    for i in range(len(matriz)):
        quantidade += len(matriz[i])
        soma += sum(matriz[i])
    media = soma / quantidade
    media = round(media, 2)
    return media