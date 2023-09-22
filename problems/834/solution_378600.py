media_matriz(matriz):
    '''Dada uma matriz de inteiros nao vazia,
    retorna a media de todos os numeros da 
    matriz
    list -> float'''
    soma = 0
    qntd_numeros = 0
    for linha in matriz:
        for coluna in linha:
            soma = soma + coluna
            qntd_numeros += 1
	media = soma/qntd_numeros
    return media